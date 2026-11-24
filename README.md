# laoliu（LaoLiuWriting，老刘）

一个 Agent Skill：按 Liu Tao 的论文写作风格，起草、修改或检查控制理论论文（TAC / Automatica）的正文和审稿回复信，同时核对数学内容，不自行创造技术名称。

风格规则来自 14 篇合作论文的整理，不是 Liu Tao 本人编写或认可的官方产品。

仓库根目录就是技能本身：

```text
SKILL.md            # 技能入口
references/         # 风格规则、记号、术语、核对清单
scripts/            # style_audit.py
README_zh-CN.md     # 技能自带的使用说明
```

## 安装

### Claude Code

```bash
git clone https://github.com/CC2001upupup/laoliu.git ~/.claude/skills/laoliu
```

只想在某个项目里用，就克隆到项目的 `.claude/skills/laoliu`。装好后用 `/laoliu`，或者在对话里说"用老刘的风格改这段"。

### Claude 网页版 / 桌面版

1. 下载并打包成 ZIP，ZIP 里应是一个 `laoliu/` 文件夹，`SKILL.md` 在它下面：

   ```bash
   git clone https://github.com/CC2001upupup/laoliu.git laoliu
   rm -rf laoliu/.git && zip -r laoliu.zip laoliu
   ```

   也可以在 GitHub 页面点 **Code → Download ZIP**，解压后把 `laoliu-main` 改名为 `laoliu` 再重新压缩。
2. 在 Settings → Capabilities 中启用 Code execution and file creation。
3. 打开 Customize → Skills，点 "+" → Upload a skill，上传 `laoliu.zip` 并启用。

### Gemini CLI / Antigravity

```bash
git clone https://github.com/CC2001upupup/laoliu.git ~/.gemini/config/skills/laoliu
```

### Codex

```bash
git clone https://github.com/CC2001upupup/laoliu.git ~/.codex/skills/laoliu
```

## 更新

用 `git clone` 装的，进入那个文件夹拉取即可：

```bash
git -C ~/.claude/skills/laoliu pull
```

把路径换成你实际装的位置。网页版 / 桌面版需要重新打包上传。

## 使用例子

> 请用 LaoLiuWriting 修改下面的 Problem Formulation。只修改这一部分，保留数学含义、符号和假设，不自行创造技术名称。先给出英文修改稿，再简短说明必要的修改。
>
> ［粘贴你的原文］

## 说明

本仓库由作者那边自动同步，内容可能随时更新。问题和建议可以提 Issue。
