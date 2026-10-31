#!/usr/bin/env python3
"""cyano-philosophy lint — 七维规范机检 + reader 对照。

规则源：.norm（命名/frontmatter/锚格式）+ 立项结构约定。
用法：python3 tools/lint.py   （退出码非零=有 FAIL）
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FAILS, WARNS = [], []
def fail(msg): FAILS.append(msg); print(f"  ✗ {msg}")
def warn(msg): WARNS.append(msg); print(f"  ⚠ {msg}")
def ok(msg): print(f"  ✓ {msg}")

TYPE_ENUM = {"readme","charter","value","axiom","criterion","protocol","evolution-doc","wiki-entry","decision-log","mapping-registry"}
NAME_RULES = [
    (re.compile(r"^c[1-9]-[a-z0-9-]+\.md$"), "criteria"),
    (re.compile(r"^p[1-9]-[a-z0-9-]+\.md$"), "protocols"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$"), "evolution"),
    (re.compile(r"^(values|worldview)\.md$"), "axioms"),
    (re.compile(r"^glossary\.md$"), "wiki"),
    (re.compile(r"^README\.md$"), None),  # 各目录索引，任意目录合法
    (re.compile(r"^(README|CHARTER)\.(zh-CN|en)\.md$"), "ROOT"),
    (re.compile(r"^(DECISIONS|MAPPING)\.md$"), "ROOT"),  # 治理台账（zh-only）  # 根级双语后缀
]
# 脱敏词表外置：tools/.sanitize-words.txt（不入仓，.gitignore 已列）——开源的 lint 不得携带待脱敏名单本身
SANITIZE_FILE = "tools/.sanitize-words.txt"
SANITIZE_WORDS = []
if os.path.exists(SANITIZE_FILE):
    SANITIZE_WORDS = [w.strip() for w in open(SANITIZE_FILE).read().split("\n") if w.strip()]
# 注：sha256 方案已否——人名空间小可暴力枚举，hash 名单=变相泄露
ANCHOR_RE = re.compile(r"〔[a-z0-9]+·[^\〕]+〕")

def md_files():
    """收集全部受检 md：根级 2 件 + zh-CN/en 内容目录。"""
    out = []
    for f in ["README.zh-CN.md","CHARTER.zh-CN.md","README.md","CHARTER.en.md","DECISIONS.md","MAPPING.md"]:
        if os.path.exists(f): out.append(f)
    for d in ["axioms","criteria","protocols","wiki","evolution"]:
        for sub in ["zh-CN","en"]:
            p = os.path.join(d, sub)
            if os.path.isdir(p):
                for fn in sorted(os.listdir(p)):
                    if fn.endswith(".md"): out.append(os.path.join(p, fn))
    return out

def check_frontmatter(path, text):
    m = re.match(r"^---\n([\s\S]*?)\n---\n", text)
    if not m:
        fail(f"{path}: 缺 frontmatter"); return None
    fm = {}
    for line in m[1].split("\n"):
        i = line.find(":")
        if i > 0: fm[line[:i].strip()] = line[i+1:].strip()
    for k in ["type","language","status","updated"]:
        if k not in fm: fail(f"{path}: frontmatter 缺 {k}")
    if fm.get("type") and fm["type"] not in TYPE_ENUM:
        fail(f"{path}: type 非法 '{fm['type']}'（枚举 {'|'.join(sorted(TYPE_ENUM))}）")
    if "/evolution/" in path and "source-date" not in fm and os.path.basename(path) != "README.md":
        warn(f"{path}: evolution 文档建议带 source-date")
    return fm

def check_name(path):
    fn = os.path.basename(path)
    if fn == "README.md": return
    for rx, where in NAME_RULES:
        if rx.match(fn):
            if where == "ROOT":
                if "/" in path: fail(f"{path}: 根级命名 {fn} 不应出现在子目录")
                return
            if where and not path.startswith(where + os.sep):
                fail(f"{path}: 命名 {fn} 属 {where} 但出现在 {path.split('/')[0]}/")
            return
    fail(f"{path}: 文件名不符合命名规范（{fn}）")

def check_links(path, text):
    body = re.sub(r"^---\n[\s\S]*?\n---\n", "", text)
    for m in re.finditer(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)", body):
        href = m.group(1)
        if href.startswith(("http://","https://","mailto:")): continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), href))
        if not os.path.exists(target):
            fail(f"{path}: 死链 {href}")

def check_mermaid(path, text):
    fences = re.findall(r"^```", text, re.M)
    if len(fences) % 2 != 0: fail(f"{path}: code 围栏不配对（{len(fences)} 个）")
    for m in re.finditer(r"```mermaid\n([\s\S]*?)```", text):
        head = m[1].strip().split("\n")[0].strip()
        if not re.match(r"^(graph|flowchart|sequenceDiagram|classDiagram|stateDiagram|erDiagram|gantt|mindmap|timeline)\b", head):
            fail(f"{path}: mermaid 块首行非图表声明 '{head[:30]}'")

ANCHOR_FULL = re.compile(r"〔[A-Za-z0-9]+ ?· ?[^〕]+〕")  # zh 紧凑·与 en " · " 皆容
ANCHOR_SHORT = re.compile(r"〔[A-Za-z0-9]+ ?〕")

def check_anchor(path, text):
    """锚检查：〔代号·节〕查格式；〔代号〕简写提示补节标识；中文行文〔〕豁免。多锚以『；』分隔时逐段查。"""
    for m in re.finditer(r"〔[^〕]+〕", text):
        seg = m[0]
        for part in re.split("[；;]", seg[1:-1]):  # 多锚分隔符：zh 全角；（U+FF1B）；en 半角 ; —— .norm 已消歧
            wrapped = f"〔{part}〕"
            if ANCHOR_FULL.match(wrapped): continue
            if ANCHOR_SHORT.match(wrapped):
                warn(f"{path}: 简写锚 '{wrapped}' 建议补节标识（〔代号·节〕）")
                continue
            if re.match(r"〔[A-Za-z0-9]+·", wrapped):
                fail(f"{path}: 锚 '{wrapped}' 格式错误")
            # 中文行文〔〕豁免

def check_sanitize(path, text):
    if not SANITIZE_WORDS:
        return  # 词表缺位：已全局 warn 一次，逐文件跳过
    hits = [w for w in SANITIZE_WORDS if w in text]
    if hits: fail(f"{path}: 脱敏命中 {hits}")

def check_ids(path, text):
    text = re.sub(r"```mermaid\n[\s\S]*?```", "", text)  # 图内节点 id（P3=第三部）非正文引用，剔除后再查
    for m in re.finditer(r"\b([CAP])-(\d+)\b", text):
        kind, n = m[1], int(m[2])
        limit = {"C": 6, "A": 4, "P": 2}[kind]
        if n < 1 or n > limit:
            fail(f"{path}: 编号引用越界 {m[0]}（现行 C1-C6/A1-A4/P1-P2）")
    for m in re.finditer(r"\b([ACP])(\d{1,2})\b", text):  # A1/C1/P1 紧凑形式（图节点/引用规范）
        kind, n = m[1], int(m[2])
        limit = {"C": 6, "A": 4, "P": 2}[kind]
        if n < 1 or n > limit:
            fail(f"{path}: 编号引用越界 {m[0]}（紧凑形式）")

def check_manifest():
    if not os.path.exists("manifest.json"):
        fail("manifest.json 不存在"); return
    with open("manifest.json") as f: mf = json.load(f)
    listed = {it["path"] for g in mf["groups"] for it in g["items"]}
    for p in listed:
        if not os.path.exists(p): fail(f"manifest: 条目不存在 {p}")
    zh = [p for p in md_files() if "/zh-CN/" in p or p.endswith(".zh-CN.md")]
    missing = [p for p in zh if p not in listed]
    if missing:
        for p in missing: fail(f"manifest: zh-CN 文件未收录 {p}")
    else: ok(f"manifest 对照一致（{len(listed)} 条 ↔ zh-CN {len(zh)} 件）")
    # en manifest 对照
    if os.path.exists("manifest.en.json"):
        with open("manifest.en.json") as f: me = json.load(f)
        listed_en = {it["path"] for g in me["groups"] for it in g["items"]}
        for p in listed_en:
            if not os.path.exists(p): fail(f"manifest.en: 条目不存在 {p}")
        INDEX_ONLY = {"axioms/en/README.md","protocols/en/README.md","wiki/en/README.md"}  # 纯索引型，导航树已含条目，不强制收录
        en_md = [p for p in md_files() if "/en/" in p and p not in INDEX_ONLY]
        miss_en = [p for p in en_md if p not in listed_en]
        for p in miss_en: fail(f"manifest.en: en 文件未收录 {p}")
        if not miss_en: ok(f"manifest.en 对照一致（{len(listed_en)} 条 ↔ en {len(en_md)} 件）")
    import subprocess
    r = subprocess.run([sys.executable, "tools/gen_manifest.py", "--check"], capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"manifest 漂移：{r.stdout.strip()[:150]}")
    else:
        ok("manifest 幂等（纯生成物，与 gen_manifest 输出一致）")

def main():
    print("═" * 6, "cyano-philosophy lint", "═" * 6)
    if not SANITIZE_WORDS:
        warn(f"脱敏词表缺失（{SANITIZE_FILE}）——脱敏检查降级跳过（开源环境预期行为）")
    # 盲区补扫：reader 部署物过词表（它们不是 md，不走七维）
    for extra in ["index.html", "manifest.json", "manifest.en.json"]:
        if os.path.exists(extra):
            with open(extra) as f: t = f.read()
            if SANITIZE_WORDS:
                hits = [w for w in SANITIZE_WORDS if w in t]
                if hits: fail(f"{extra}: 脱敏命中 {hits}")
    files = md_files()
    print(f"受检 {len(files)} 件 md\n── frontmatter / 命名 / 链接 / mermaid / 锚 / 脱敏 / 编号 ──")
    for p in files:
        with open(p) as f: text = f.read()
        check_frontmatter(p, text)
        check_name(p)
        if "/en/" not in p and os.environ.get("LINT_EN_SKIP") != "1":  # en 默认同标准检查；LINT_EN_SKIP=1 可退回 zh-only
            check_links(p, text)
            check_mermaid(p, text)
            check_anchor(p, text)
            check_sanitize(p, text)
            check_ids(p, text)
    print("── manifest 对照 ──")
    check_manifest()
    print("═" * 30)
    print(f"结果：{len(FAILS)} FAIL / {len(WARNS)} WARN")
    if FAILS:
        print("存在 FAIL，退出码 1"); sys.exit(1)
    print("全绿 ✅")

if __name__ == "__main__":
    main()
