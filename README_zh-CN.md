# LaoLiuWriting（laoliu-writing）：Claude 导入与使用

更新日期：2026-09-08。本 skill 由两部分合并而成：

1. **Liu Tao Tone 风格层**（`references/` 中 7 份文件）：基于 14 篇合作论文提炼的写作架构、各模块 playbook、语言规则和证据边界。不是 Liu Tao 本人编写或认可的官方产品。
2. **正确性层**（`references/` 中 4 份文件，继承自原 `control-theory-writing` skill）：验证清单（数值核对、Zotero 引文核对、假设–证明匹配）、LaTeX 记号约定、术语一致性、期刊格式规则。

两层冲突时以 SKILL.md 中 "Precedence between the two layers" 为准：不自行创造技术名称；`Substituting ... gives [display]` 之类带谓语的结构可以接公式；定理陈述保留关键有效性条件；Remark 可以放在定理前、可以讨论排除的情形；roadmap 与长句按功能决定。`terminology.md` 中的具体选词（network/topology、semisimple 等）是自己稿件的默认值，不得据此改动他人稿件的数学含义。

## Claude 网页版 / 桌面版

1. 在 Settings → Capabilities 中启用 Code execution and file creation。
2. 打开 Customize → Skills，选择 "+" → "Create skill" → "Upload a skill"。
3. 上传 `laoliu-writing.skill`（ZIP）并启用。不需要先解压，也不要只上传 SKILL.md。
4. 如已安装旧版 `control-theory-writing`，建议禁用或删除，避免两套规则同时触发。
5. 对话里说明使用 LaoLiuWriting / 老刘 tone，提供要写或修改的段落及必要事实。

## Claude Code

解压后将整个 `laoliu-writing` 文件夹放到 `~/.claude/skills/` 或项目的 `.claude/skills/`，最终结构为 `.claude/skills/laoliu-writing/SKILL.md`。然后使用 `/laoliu-writing`，后接写作要求和材料。

## 关于名称

frontmatter 的 `name` 必须是小写字母、数字和连字符（skill 规范要求），所以文件夹和 `name` 用 `laoliu-writing`；`LaoLiuWriting` 和 `老刘` 写在标题与描述里，对话中直接说 LaoLiuWriting 即可触发。

## 一个使用例子

> 请用 LaoLiuWriting 修改下面的 Problem Formulation。只修改这一部分，保留数学含义、符号和假设，不自行创造技术名称。先给出英文修改稿，再简短说明必要的修改。
>
> ［粘贴你的原文］

写新段落时，提供该段所需的问题、方法、已证明结果和条件即可。若只想分析，明确说"只分析，不重写"。

## 包含什么

- SKILL.md：入口、两层规则的优先级、模块导航。
- references/：11 份规则文件。
- scripts/style_audit.py：可选本地检查脚本，仅在明确请求风格审查时使用；Python 3 标准库，不联网、不修改稿件。
- 本说明文件。

规则里的 C01–C14 是原分析语料的内部编号。skill 不附带原始论文 PDF，也不是数学正确性认证；结果仍需按稿件与证明核对。
