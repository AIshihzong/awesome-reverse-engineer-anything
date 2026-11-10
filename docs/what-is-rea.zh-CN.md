# REA（Reverse Engineer Anything）是什么？常见问题

[English](what-is-rea.md) · **简体中文** · [返回主列表](../README.zh-CN.md)

> [在 GitHub 上点个 ⭐](https://github.com/AIshihzong/awesome-reverse-engineer-anything)方便下次找到，或者 **Watch → Custom → Releases** 订阅 [AI 逆向周报](https://github.com/AIshihzong/awesome-reverse-engineer-anything/releases)。

关于 REA 最常被问到的问题，每条都附来源链接。事实已在主列表中核查过；Star 数和版本每周都在变，请看数字旁边的日期。

## REA 是什么？

REA 是 **Reverse Engineer Anything**（逆向一切）的缩写，指 [morluto/rea](https://github.com/morluto/rea)：一个开源（MIT）的 MCP 服务器和命令行工具。它让编程 Agent 在没有源代码的情况下检查原生二进制、Electron 应用、.NET 程序集、安卓 APK、固件和网站，用证据解释某个功能如何工作，并重建它。截至 2026-11-01，它在 GitHub 上有 41.7 万以上的 Star。

## REA 自己会反编译吗？

不会。REA 为 Agent 调度 Hopper、Ghidra、IDA、JADX 等现有工具，并把它们的结果整理成证据。

## 怎么安装 REA？

官方发布的包是 [npm 上的 `rea-agents`](https://www.npmjs.com/package/rea-agents)。运行 `npx rea-agents setup` 就能把它注册到你的 Agent。官方文档在 [rea.tools](https://rea.tools/)，有[图文教程](https://rea.tools/guides/)，也有[中文 README](https://github.com/morluto/rea/blob/main/docs/readme/README_zh.md)。

## 从哪里下载才安全？

只从 [morluto/rea](https://github.com/morluto/rea)、[rea.tools](https://rea.tools/) 和 npm 包 `rea-agents` 获取。GitHub 上有一些名字相近的仓库，声称提供"官方免费下载"的 zip 文件，它们不是官方渠道。不要运行其他地方的压缩包或可执行文件。

## 在自己电脑上运行 REA 安全吗？

分析在本地运行，但工具结果会经过 Agent 发送给模型服务商。REA 自己的 SECURITY.md 写明 REA 不是沙箱。它能调用的商业工具，如 IDA Pro、Hopper 和 JEB，需要另外购买授权；REA 不提供授权。

## 用 REA 合法吗？

逆向工程受当地法律、软件许可和服务条款约束。REA 的 [DISCLAIMER.md](https://github.com/morluto/rea/blob/main/DISCLAIMER.md) 列出的允许用途是：学习、研究、互操作、保存、安全研究、漏洞披露和 CTF；不包括复制专有软件或复现其受保护的代码和素材。详见[合规与争议](../README.zh-CN.md#合规与争议)。

## REA 被用来做过什么？案例

官方[案例展示](https://rea.tools/showcase/)包括：逐字节重建 DX-Ball 的一个声音函数、追踪 Notion 的 Electron 剪贴板桥接、追踪 Aegis 安卓应用的 TOTP 验证码生成。社区里自称用了 REA 的项目有 .NET 取色器 [hexgrab](https://github.com/iammukeshm/hexgrab)、macOS 上的 Rust 录屏工具 [rec-rs](https://github.com/michaelshimeles/rec-rs) 等。完整列表见主列表的[社区案例](../README.zh-CN.md#社区案例用-rea-做出来的东西)和[按软件索引](by-app.zh-CN.md)。

## 那些爆火的演示真的用了 REA 吗？

很多没有。[传播最广的六个案例](../README.zh-CN.md#先看这些)里，只有 DX-Ball 在自己的仓库里写明用了 REA；另外两个只在作者帖子里这么说，其余三个用了别的工具或尚未核实。[真的用了 REA 吗？](is-it-rea.zh-CN.md)逐条对照来源核查。

## REA 能克隆整个应用或还原源代码吗？

官方项目两者都没有声称。DX-Ball 的数字（3,205 个测试用例一致、63 字节一致）只针对一个函数，不是整个游戏。

## REA 真的能帮到 Agent 吗？

我们所知的对照测试结论不一。[rea-lab](https://github.com/pablodiazjorge/rea-lab) 用 Claude Code 跑了 482 次，没有发现解题率有显著提升，而且用 REA 的运行时间和成本约为两倍。[leanrea](https://github.com/aicodeking/leanrea) 发现一个纯命令行的 skill 准确率接近 REA，成本更低。详见[对照实验](../README.zh-CN.md#rea-到底有没有用对照实验)。

## REA 还是 Craft Anything？

REA 解释程序如何工作并给出证据；Craft Anything 让 Agent 做出你自己的版本，再和原版对照检查。见 [REA 还是 Craft Anything？](rea-vs-craft-anything.zh-CN.md)

## 在哪里提问？

官方 [Discord](https://discord.gg/GkcryMnJDM)（问答和作品展示频道）以及 [GitHub Discussions](https://github.com/morluto/rea/discussions)。本 FAQ 和列表是非官方的，与 morluto/rea 无关。
