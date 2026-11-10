# REA 还是 Craft Anything？

[English](rea-vs-craft-anything.md) · **简体中文**

> [在 GitHub 上点个 ⭐](https://github.com/AIshihzong/awesome-reverse-engineer-anything)方便下次找到，或者 **Watch → Custom → Releases** 订阅 [AI 逆向周报](https://github.com/AIshihzong/awesome-reverse-engineer-anything/releases)。

两个项目都通过 MCP 和 CLI 给编码 Agent 提供逆向工具，也都是 2026 年秋天 GitHub 上涨得最快的仓库之一。但它们回答的是不同的问题。**REA 告诉你一个程序是怎么工作的，并给出证据。Craft Anything 拿到一个目标后，让 Agent 做出你自己的版本，再拿它和原版比对。**

下面的内容都来自两个项目自己的 README，读取时间是 2026-11-09。两边更新都很快，引用细节前请再看一眼原文。两个项目都没有提到对方。

## 一览

|           | [REA](https://github.com/morluto/rea)                   | [Craft Anything](https://github.com/storytold/craft-anything)                |
| --------- | ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 产出        | 带证据和局限说明的结论，由 Agent 决定下一步                               | `app/` 里的新项目，加上与原版的比对结果和收集到的证据                                               |
| 工作流       | Agent 提问，REA 检查和追踪，Agent 解释、实现、测试                       | 研究 → 构建 → 比对 → 交付，循环到足够接近为止                                                  |
| 形态        | MCP Server 和 CLI（`npx rea-agents setup`）                | 桌面应用（简单和高级两种模式）、CLI 和 MCP Server；提供 Windows、macOS、Linux、FreeBSD 安装包          |
| 语言        | Node.js                                                 | Rust                                                                         |
| 分析引擎      | 原生代码用你装好的 Hopper、Ghidra、IDA 或 Kuna；JavaScript 分析不需要额外引擎 | 自带解码器、反汇编器和反编译器；Deep 模式下装了 Ghidra 也会用                                        |
| 目标类型      | 原生二进制、JavaScript/Electron、.NET、网站等                      | 原生程序、.NET、Java、Android、Apple、Electron、网站、固件、抓包文件、数据库、游戏文件                    |
| 工具数量      | 由生成的目录列出，未提交到仓库                                         | 约 320 个（引擎 302 个，分 17 组）                                                     |
| 支持的 Agent | Claude Code、Codex、Cursor、Gemini CLI、Grok Build 等        | 首选 Claude Code；Copilot、Grok Build 和其他 ACP Agent 部分验证                         |
| 默认立场      | 以证据为先，分析你指定的目标                                          | 净室：只看访客能看到的内容；Deep 模式才读代码和文件                                                 |
| 成熟度       | 发版频繁（v5 在 2026 年 10 月走红）                                | 早期 alpha，2026-10-31 创建                                                       |
| 许可证       | MIT                                                     | MIT 或 Apache-2.0                                                             |
| 作者        | morluto                                                 | ArtCraft 团队，也是 [Craft 系列应用](../README.zh-CN.md#同一波浪潮未写明使用-rea-的-ai-逆向项目) 的作者 |

## 该选哪个

- **想搞懂一个功能、协议或文件格式**，然后自己或让 Agent 写代码：选 REA。它擅长有针对性的问题，返回的证据 Agent 可以直接引用。[rea-lab 的实验](https://github.com/pablodiazjorge/rea-lab) 显示，它在已知范围内的定向问题上最划算，开放式探索反而不占优。
- **想要一个能用的网站、应用或游戏复刻，用你指定的技术栈**：选 Craft Anything。"构建再比对"这个循环，正是 REA 留给 Agent 自己做的部分。
- **在意法律风险**：Craft Anything 默认的净室模式会拒绝调用读取目标内部的工具。这是它对自身功能的约束，不是系统沙箱，README 里也这样写明了。REA 没有这种模式，检查什么由你决定。两者都不能让重建本身变得合法，见 [合规与争议](../README.zh-CN.md#合规与争议)。
- **需要图形界面**：Craft Anything 自带。REA 可以用社区做的 [marrow](https://github.com/utabk/marrow)。

## 本列表怎么标注

只有来源写明用了 morluto/rea 的案例才标 `REA`。用 Craft Anything 做出来的项目先标 `AI 逆向`，等这类案例多到值得单独设标签时再调整。如果你用其中任何一个做出了东西，欢迎 [提交案例](https://github.com/AIshihzong/awesome-reverse-engineer-anything/issues/new?template=case.yml)。
