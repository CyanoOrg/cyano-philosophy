---
type: decision-log
language: zh-CN
status: draft
updated: 2026-10-31
---

# DECISIONS —— 治理决策账本

> append-only：只追加，不改写。每条治理决策（正典修订终裁/许可变更/治理规则本身的变化）在此留痕。格式：编号 / 日期 / 决策 / 依据 / 流程记录（提案→反驳期→终裁）。

| # | 日期 | 决策 | 依据 | 流程记录 |
|---|---|---|---|---|
| D-001 | 2026-10-30 | 分层许可落地：文本 CC BY-SA 4.0（根 LICENSE）+ 代码 MIT（tools/LICENSE） | 开源宣言无 LICENSE = 默认全保留，与公开目的自相矛盾；分层方案与「文本共享/工具自由」的意图对齐 | 终裁豁免追补：决策当时本账本未建，owner 直接终裁落地（2026-10-30）；本条为追溯补录（2026-10-31），此后治理动作均先立记录 |
| D-002 | 2026-10-31 | 仓库架构：GitHub CyanoOrg/cyano-philosophy 为唯一主仓与公开工作面（main 保护：禁 force-push/禁删）；Pages 为阅读器入口；不设第二权威拷贝 | 公开性是宣言的本质需求；禁 force-push 是演化档案 append-only 的 git 层硬保障 | owner 与执行者（huimu）协商定案（对话留痕于工作日志）；规范落于 .norm repo_management |
