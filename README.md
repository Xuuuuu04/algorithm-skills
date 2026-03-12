# algorithm-skills

这是一个面向华为 ICT 仓颉比赛的 OpenCode 竞赛工作仓库。仓库的目标不是单纯堆 Skill，而是把 `AGENTS.md`、`.opencode/oh-my-opencode.jsonc`、`.claude/agents/`、`.claude/skills/` 组织成一套可直接上手的比赛代理系统，让队友在 OpenCode 里打开仓库后，就能按统一流程处理 `ACM`、`LeetCode`、`项目开发` 三类任务。

如果你们已经在用 OpenCode，并安装了 `oh-my-opencode` / `oh-my-openagent`，这个仓库会自动提供项目级配置、项目级自定义代理、仓颉 Skill 知识库和比赛纪律约束。仓库已经把“模式识别、题面核验、算法对抗审查、仓颉实现审计、项目结构侦察、最终交付门禁、失败反馈分诊”这些关键步骤接进了代理链路，不需要队友自己从零摸索。

## 快速开始

根据 Oh My OpenAgent 官方文档，最简单的安装方式是先运行：

```bash
bunx oh-my-opencode install
```

官方文档说明，项目级配置文件位置是 `.opencode/oh-my-opencode.json`，并且支持 JSONC。本仓库已经提供了项目级配置文件 [`.opencode/oh-my-opencode.jsonc`](/Users/xushaoyang/Desktop/algorithm-skills/.opencode/oh-my-opencode.jsonc)，所以安装完成后，直接把仓库打开到 OpenCode 里即可。

推荐的上手顺序如下。

第一步，克隆仓库并进入目录。

```bash
git clone https://github.com/Xuuuuu04/algorithm-skills.git
cd algorithm-skills
```

第二步，用 OpenCode 打开这个仓库，并确认它能看到项目级配置、项目级 agents 和 `.claude/skills` 目录。

第三步，直接用自然语言提任务，不要自己先决定怎么路由。这个仓库里的代理系统会先判断当前是 `ACM`、`LeetCode`、`项目开发` 还是 `测试反馈`，再决定应该走哪条链路。

## 仓库会自动帮你做什么

这个仓库不是只有一个总的 `AGENTS.md`。真正起作用的是四层结构。

第一层是根规则 [AGENTS.md](/Users/xushaoyang/Desktop/algorithm-skills/AGENTS.md)。它定义了三种任务模式、目标路径、禁止行为、OpenCode 代理协作顺序和最终输出协议。

第二层是项目级 OpenCode 配置 [`.opencode/oh-my-opencode.jsonc`](/Users/xushaoyang/Desktop/algorithm-skills/.opencode/oh-my-opencode.jsonc)。它会细化内置代理，例如 `Sisyphus`、`Prometheus`、`Metis`、`Momus`、`Oracle`、`Librarian`、`Explore`、`Atlas`，并把比赛专用 custom skills 挂到这些代理上，让它们默认遵守本仓库的纪律，而不是按泛用模式随便发挥。

第三层是项目级自定义代理目录 [`.claude/agents`](/Users/xushaoyang/Desktop/algorithm-skills/.claude/agents)。这里放的是比赛专用子代理，例如：

`contest-mode-router` 负责先判定任务模式和目标路径。  
`statement-verifier` 负责把题库索引、镜像链接、外部摘要继续核成正文级事实。  
`algorithm-adversary` 负责高难算法题的反例、退化和复杂度攻击。  
`cangjie-implementation-auditor` 负责仓颉语法、API、import、构建和 `cjpm` 依据审计。  
`project-structure-scout` 负责项目模式下参考 CangjieSIG 活跃仓库给出结构建议。  
`delegate-prompt-composer` 负责把模糊任务改写成高质量委派 prompt。  
`contest-final-gate` 负责交付前做最终门禁。  
`test-feedback-triage` 负责在 `WA/TLE/RE/MLE/CE` 或项目报错后先分诊再修。

第四层是 [`.claude/skills`](/Users/xushaoyang/Desktop/algorithm-skills/.claude/skills)。这里是仓颉和比赛知识底座，包括算法核心 Skill、仓颉语言和标准库 Skill、题库实体集合、CangjieSIG 活跃仓库参考集合等。只要是仓颉语法、标准库 API、`cjpm`、项目组织规范、题库正文、外部事实，默认都要先回到这些 Skill 或进一步联网复核，而不是靠记忆写。

## 三种任务怎么用

### ACM 题

对于 ACM 题，你只要把完整题面、输入输出、样例发给 OpenCode 即可。系统会默认把目标落在 [src/main.cj](/Users/xushaoyang/Desktop/algorithm-skills/src/main.cj)，然后按这条链路推进：

`contest-mode-router → statement-verifier → algorithm-adversary → cangjie-implementation-auditor → 实现 → contest-final-gate`

这条链路的意义是：先确认题面正文和约束，再挑战算法本身，再核对仓颉实现，最后才允许交付。这样可以尽量减少“题意看错”“复杂度看错”“仓颉 API 写错”这三类比赛里最容易翻车的问题。

### LeetCode 题

对于 LeetCode 题，你也可以直接把链接、题意、函数签名或英文原题发进来。系统会先把题目抽象成算法模型，再映射到本地仓颉实现。工作区内的权威实现仍然落在 [src/main.cj](/Users/xushaoyang/Desktop/algorithm-skills/src/main.cj)，但最终回复时会额外说明如何映射回平台提交格式。

推荐链路是：

`contest-mode-router → statement-verifier（如题意来自外链）→ algorithm-adversary → cangjie-implementation-auditor → 实现 → contest-final-gate`

### 项目开发题

如果题目实际上是“做系统”“写服务”“写 SDK”“写 CLI”“做模块化工程”，系统会优先判定成项目模式，而不是硬塞进 `src/main.cj`。没有现成项目目录时，默认会建议在 `projects/<slug>/` 下新建独立仓颉项目。

推荐链路是：

`contest-mode-router → project-structure-scout → delegate-prompt-composer → 实现/修改 → cangjie-implementation-auditor → contest-final-gate`

这意味着项目模式会先参考 CangjieSIG 活跃仓库样本和 `cangjie-project-management` Skill，再决定目录结构、`cjpm.toml`、测试和构建方式，而不是随便生成一个看似高级但不贴仓颉生态的项目壳子。

## 出现 WA / TLE / RE / CE 之后怎么办

你们不需要手动告诉代理“去猜一下哪里错了”。这个仓库已经给测试反馈准备了专用链路：

`contest-mode-router → test-feedback-triage → 必要时 statement-verifier / algorithm-adversary / cangjie-implementation-auditor → 修复 → contest-final-gate`

也就是说，一旦出现 `WA/TLE/RE/MLE/CE`、编译错误、运行日志、项目测试失败，系统会先分诊，再决定优先回查哪个 Skill、先复现什么、先修什么，尽量避免盲修造成二次错误。

## OpenCode 使用建议

在这个仓库里，最重要的不是“多叫代理”，而是“让代理在正确的顺序里做正确的事”。因此推荐你们遵守几个简单习惯。

第一，不要一上来就自己指定最终方案。先把题目或需求完整发出来，让系统先判模式。

第二，只要信息来自题库索引、镜像页、仓库摘要、版本列表、快照文档，就默认它还不是最终事实。这个仓库已经把“需要继续 `fetch/search` 复核”写进了配置和代理纪律里，所以你们应该鼓励它去核，而不是要求它省略这一步。

第三，如果你们想让子代理工作得更稳，最好让主代理先经过 `delegate-prompt-composer`。这样委派 prompt 会更细，输出质量通常会更稳定。

第四，在准备提交答案或发给队友之前，尽量让系统经过一次 `contest-final-gate`。这一步的价值很高，因为很多表面上看起来“差不多”的结果，实际上还存在模式错误、路径错误、未核验事实或验证不足的问题。

## 关键文件一览

如果队友第一次接手这个仓库，最值得先看的文件是这些。

[AGENTS.md](/Users/xushaoyang/Desktop/algorithm-skills/AGENTS.md) 负责总协议。  
[README.md](/Users/xushaoyang/Desktop/algorithm-skills/README.md) 负责上手说明。  
[.opencode/oh-my-opencode.jsonc](/Users/xushaoyang/Desktop/algorithm-skills/.opencode/oh-my-opencode.jsonc) 负责项目级 OpenCode 编排配置。  
[.claude/agents](/Users/xushaoyang/Desktop/algorithm-skills/.claude/agents) 负责项目级自定义代理。  
[.claude/skills](/Users/xushaoyang/Desktop/algorithm-skills/.claude/skills) 负责仓颉和比赛知识库。  
[src/main.cj](/Users/xushaoyang/Desktop/algorithm-skills/src/main.cj) 是 ACM / LeetCode 的统一落点。  
[cjpm.toml](/Users/xushaoyang/Desktop/algorithm-skills/cjpm.toml) 是当前工作区的仓颉包配置。

## 题库与参考资产说明

这个仓库里已经包含了比赛强化参考资产，不只是 Skill 文本。

Codeforces 题库、题面实体文档、题面快照、答案入口索引都在 `cj-codeforces-1800-2400` Skill 下。当前重点区间 `1800-2400` 已经是全量真实题面正文。全量 Codeforces 则是“能抓到的尽量抓成正文，抓不到的保留索引型单题文档”。

CangjieSIG 活跃仓库参考集合在 `cj-cangjiesig-active-repos` Skill 下，已经整理成一项目一个目录的实体集合。项目模式下，代理会优先参考这些仓库来决定组织规范，而不是凭空搭结构。

## 给队友的最短操作建议

如果你只想告诉队友一句怎么用，可以直接发这段：

“先安装 `oh-my-opencode`，再用 OpenCode 打开这个仓库，直接把题目或需求发进去，不要自己手动选模式。这个仓库会自动区分 ACM / LeetCode / 项目开发，并用项目级代理去做题面核验、算法审查、仓颉实现审计和最终门禁。算法题统一落在 `src/main.cj`，项目题会单独建项目目录。”
