# 真的用了 REA 吗？

[English](is-it-rea.md) · **简体中文**

> [在 GitHub 上点个 ⭐](https://github.com/AIshihzong/awesome-reverse-engineer-anything)方便下次找到，或者 **Watch → Custom → Releases** 订阅 [AI 逆向周报](https://github.com/AIshihzong/awesome-reverse-engineer-anything/releases)。

很多案例都写着"用 REA 做的"。这一页把每个案例和项目自己的 README、作者帖子或官方案例逐一对照，并记录结果。首次核对于 2026-10-14；2026-11-10 又对照每个仓库当前的 README 和 Agent 说明文件重新核对了「README 写明用了 REA？」一栏，没有变化。我们的环境无法打开 X 帖子，所以对于 X 上的案例，我们依据的是表格里注明的第三方案例记录。

**汇总（共 39 行，2026-11-10）：**

- **26 个确认：** README、Agent 说明文件（AGENTS.md、CLAUDE.md）或官方案例写明用了 REA。
- **3 个部分使用：** 只有一部分工作用了 REA。
- **4 个未核实：** 2 个只有作者帖子里的说法，2 个找不到说明用了什么工具的来源。
- **6 个不是 REA：** 用的是其他 AI 工具（多数是 Claude Code 或 Codex 配 Ghidra、IDA），或者是手工逆向。

REA 到底有没有帮助是另一个问题。本列表收录的两组对照实验，[rea-lab](https://github.com/pablodiazjorge/rea-lab)（482 次预注册运行）和 [leanrea](https://github.com/aicodeking/leanrea)（36 次运行），都没有发现 REA 显著提高解题率，而且时间和成本更高。两者样本都不大。详见[REA 到底有没有用：对照实验](../README.zh-CN.md#rea-到底有没有用对照实验)。

| 案例                                                                                         | README 写明用了 REA？                   | 其他来源                                | 结论                                                                             |
| ------------------------------------------------------------------------------------------ | ---------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------ |
| [DX-Ball](https://github.com/N0zoM1z0/dx-ball)                                             | 是                                  | 官方案例                                | **已确认。** 一个函数逐字节对上，整款游戏尚未完成。                                                   |
| [TH04](https://github.com/N0zoM1z0/th04)                                                   | 否                                  | 官方案例                                | **仅在官方案例的检查中用过 REA。** 复原由 Agent 产出，以 ReC98 为基础。                                |
| 其他东方仓库（th08、th09、th10、th095、th105、th08-web、factory）                                        | 否                                  | 作者的 AGENTS.md 写明使用 IDA MCP / Ghidra | **不是 REA。** 标注为 AI 逆向。                                                         |
| [rec-rs](https://github.com/michaelshimeles/rec-rs)                                        | 是                                  | —                                   | **已确认。** OBS 是 GPL 许可，README 说明只研究了架构。                                         |
| [paper-rs](https://github.com/michaelshimeles/paper-rs)                                    | 是                                  | —                                   | **已确认。**                                                                       |
| [terminal-rs](https://github.com/michaelshimeles/terminal-rs)                              | 是                                  | —                                   | **已确认。** 只使用公开的 TradingView 页面。                                                |
| [wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown)               | 是                                  | —                                   | **已确认。** 按照一段教程视频进行。                                                           |
| [ledger-reborn](https://github.com/lxistired/ledger-reborn)                                | 是                                  | Discussion #2198                    | **已确认。**                                                                       |
| [AdamTerm](https://github.com/AdamLinCodes/AdamTerm)                                       | 是                                  | —                                   | **已确认。**                                                                       |
| [hexgrab](https://github.com/iammukeshm/hexgrab)                                           | 是                                  | —                                   | **已确认。**                                                                       |
| [baocut](https://github.com/JimLiu/baocut)                                                 | 否                                  | 作者的 X 帖子；提交 b8585e0                 | **作者说用了，但 README 没写。** REA 只涉及一次提交，不是整个仓库。                                     |
| [zee-rp](https://github.com/LilZeeCN/zee-rp)                                               | 否                                  | 作者在 X 上的回复                          | **作者说用了。** 只在 macOS 上验证过。                                                      |
| [cameo](https://github.com/wquguru/cameo)                                                  | 否                                  | 作者后续的 X 帖子                          | **未确认。** 链接的仓库是原创应用，不是 REA 的产出。                                                |
| [vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux)                        | 是                                  | —                                   | **已确认。** 尚未在真实头显上测试。                                                           |
| [GunZRs](https://github.com/OpenRsG/GunZRs)                                                | 是                                  | —                                   | **已确认。** 移植中 REA 的作用有限（可执行文件有加壳）。                                              |
| [OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2)                           | 否（写在 CLAUDE.md 和 `tools/rea.sh` 里） | —                                   | **用了 REA，但 README 没写。**                                                        |
| [desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia)               | 是                                  | —                                   | **已确认。**                                                                       |
| [rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | 是                                  | —                                   | **已确认。**                                                                       |
| [netcat-openbsd 分析](https://github.com/NullLabTests/OpenBSD_netcat_REA)                    | 是                                  | —                                   | **已确认。**                                                                       |
| [REA-demo](https://github.com/az9713/REA-demo)                                             | 是                                  | —                                   | **已确认。**                                                                       |
| [rea-groundtruth](https://github.com/UnknownHacker1/rea-groundtruth)                       | 是                                  | —                                   | **已确认。**                                                                       |
| [rea-safe-agents](https://github.com/dagoSte/rea-safe-agents)                              | 是                                  | —                                   | **已确认。** 固定 REA 6.7.0 并把它放进受限容器运行。它的贡献在隔离本身，不在分析。                              |
| [blender-agent-sdk](https://github.com/yazzang-homelab/blender-agent-sdk)                  | 是                                  | —                                   | **已确认。** 用 REA 的 Ghidra provider 分析剥离后的 Blender 5.2.2 二进制；证据与边界说明都在仓库里。        |
| [calendar-reconstruction](https://github.com/E2-Veera/calendar-reconstruction)             | 是                                  | —                                   | **已确认。** 用 REA（rea-agents 6.5.0）对 Calendar.app 做静态分析和界面采集，摘要在 `evidence/rea/`。 |
| [mucrab](https://github.com/soyrochus/mucrab)                                              | 是                                  | —                                   | **部分。** REA 负责清点 JAR、核对类指纹；方法还原用 CFR 和 `javap`。                                |
| [feature-heist](https://github.com/devtechedge/feature-heist)                              | 是                                  | —                                   | **已确认。** 每个重写都写明用了哪条 REA 命令；REA 记录存档并记录 SHA-256。                               |
| [bla](https://github.com/qybaihe/bla)                                                      | 是                                  | —                                   | **已确认（作为测试对象）。** BLA 不是用 REA 做的；它的红队脚本用真实 REA 分析加固后的样例。                        |
| [quicken-2002-dumper](https://github.com/bitwisecook/quicken-2002-dumper)                  | 是                                  | —                                   | **已确认（未附链接）。** README 和格式说明写明用了 `reverse-engineer-anything`，但没有链接 morluto/rea。 |
| [agent-sandbox](https://github.com/lalbers/agent-sandbox)                                  | 是                                  | —                                   | **已确认。** 它隔离运行的 MCP 服务器就是 REA。                                                 |
| [papertrade-research](https://github.com/KoNit-K/papertrade-research)                      | 是                                  | —                                   | **已确认。** 有一篇研究笔记专门记录 REA 对前端和合约的交叉核对。                                          |
| [xid8300-linux](https://github.com/Shirozo/xid8300-linux)                                  | 是                                  | —                                   | **已确认。** README 的“How it was made”写明由 Claude Code 驱动 REA 分析 Windows 驱动。        |
| [a6000-fw-decomp](https://github.com/nicolvus/a6000-fw-decomp)                             | 仅 Agent 说明                         | —                                   | **在 AGENTS.md 中确认。** 写明“先用 REA”，Ghidra 作备用；README 未提及。                         |
| [VSL-DSP](https://github.com/grisuno/VSL-DSP)                                              | 是                                  | —                                   | **部分确认。** REA 只帮忙找到了一些厂商相关的发现；该仓库早于 REA。                                       |
| [plx-native](https://github.com/GLinnik21/plx-native)                                      | 否                                  | 转述的帖子说用的是 Ghidra + Claude Code      | **不是 REA。** 标注为 AI 逆向。                                                         |
| [rea-video](https://github.com/JuneYaooo/rea-video)                                        | 否                                  | —                                   | **不是 REA。** 只是名字前缀相同，项目无关：它拆解的是视频，不是软件。标为 AI 逆向。                               |
| [open-appleremote](https://github.com/a-funk/open-appleremote)                             | 否                                  | 作者的帖子没有说明用了什么工具                     | **未确认。**                                                                       |
| [universal-modder](https://github.com/rehan-remade/universal-modder)                       | 否                                  | 帖子早于 REA 4.0                        | **不是 REA。** 标注为 AI 逆向。                                                         |
| [OpenGHub](https://github.com/Slyvan25/OpenGHub)                                           | 否                                  | 任何地方都没提 AI 或 REA                    | **不是 REA。** 基于抓包的人工逆向。                                                         |
| Firefighter（X）                                                                             | —                                  | 转述记录                                | **不是 REA。** 标注为 AI 逆向。                                                         |
| 《现代战争 2》反编译（X）                                                                             | —                                  | 转述记录                                | **不是 REA。** 标注为 AI 逆向。                                                         |

如果你发现这里有错误的案例，请使用案例表单提交 Issue。
