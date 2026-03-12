---
name: cj-doc-evidence-citation
description: 仓颉文档证据引用技能。用于定义算法题中的最小证据集、三段引用格式与校验策略，并按 lite 或 strict 模式决定引用强度；不负责整体答案结构。
---

# Evidence Citation

本 Skill 只处理“哪些结论必须引用、引用格式是什么、如何校验”。答案结构由 `cj-ice-contest-protocol` 负责。

## 模式联动

### `strict`
- 至少 2 条引用，默认要求 1 条语法 + 1 条 API
- 正式题解、教学、复盘、评测场景必须执行

### `lite`
- 只有在做出非显然语法、API、复杂度或异常行为结论时才强制引用
- 如果答案只是直接给标准模板代码且没有额外库结论，可不单列引用段

## 三段引用规范
每条关键结论使用一行:
```
path | anchor | "quote"
```

### 字段说明
| 字段 | 要求 | 示例 |
|------|------|------|
| path | 技能目录内文档相对路径 | `cj-std-algo-toolkit/references/docs/std/collection/collection_package_api/collection_package_class.txt` |
| anchor | 标题锚点或原始标题 | `class-arraylist` 或 `ArrayList` |
| quote | 原文短引 (≤30 字) | `"ArrayList 是一个可动态扩展的数组"` |

### 格式示例
```
cj-std-algo-toolkit/references/docs/std/sort/sort_package_api/sort_package_funcs.md | func-sort | "对 Array 进行排序"
cj-language-core/references/docs/user_manual/function/define_functions.md | 函数定义 | "使用 func 关键字定义函数"
```

## 引用分类

### 必须引用的场景
1. **语法规则** — 引用 cj-language-core 下 user_manual/ 对应章节
2. **API 行为** — 引用 cj-std-algo-toolkit 下 std/ 对应模块文档
3. **复杂度声明** — 引用文档中复杂度描述 (如有)
4. **类型约束** — 引用泛型/接口要求
5. **异常行为** — 引用 throws/异常类文档

### 最少引用数
- strict 标准答案: ≥ 2 条 (1语法 + 1API)
- strict 深度答案: ≥ 4 条
- lite: 按需，只有出现关键非显然结论时才要求引用

## 文档路径速查 (相对 `.claude/skills/`)
| 内容 | 路径前缀 |
|------|---------|
| 语法/类型/控制流 | `cj-language-core/references/docs/user_manual/` |
| 标准库 API (竞赛核心) | `cj-std-algo-toolkit/references/docs/std/` |
| 标准库 API (非核心) | `cj-doc-indexer/references/docs/std/` |
| 扩展库 API | `cj-stdx-reference/references/docs/libs_stdx/` |
| 高频模块: collection | `cj-std-algo-toolkit/references/docs/std/collection/` |
| 高频模块: sort | `cj-std-algo-toolkit/references/docs/std/sort/` |
| 高频模块: math | `cj-std-algo-toolkit/references/docs/std/math/` |
| 高频模块: overflow | `cj-std-algo-toolkit/references/docs/std/overflow/` |
| 高频模块: convert | `cj-std-algo-toolkit/references/docs/std/convert/` |

## 校验
```bash
python3 scripts/validate_evidence.py \
  --index <doc_index.jsonl> \
  --answer-file <answer.md> \
  --strict
```

## 失败标记
| 错误类型 | 标记 |
|---------|------|
| 路径不存在 | `path_not_found_in_index` |
| 锚点不匹配 | `anchor_not_found` |
| 引用缺段 | `citation_requires_3_parts` |
| 引用伪造 | `quote_not_verified` |

## 不确定处理
当无法确认文档中存在对应内容时:
```
cj-[skill]/references/docs/... | ... | "[不确定] ..."
```
明确标注，不伪造引用。
