# REA or Craft Anything?

**English** · [简体中文](rea-vs-craft-anything.zh-CN.md)

> ⭐ [Star the list on GitHub](https://github.com/AIshihzong/awesome-reverse-engineer-anything) to find it again, or **Watch → Custom → Releases** for the [weekly digest](https://github.com/AIshihzong/awesome-reverse-engineer-anything/releases).

Both projects give a coding agent reverse-engineering tools over MCP and a CLI, and both were among GitHub's fastest-growing repos in autumn 2026. They answer different questions. **REA explains how a program works and shows the evidence. Craft Anything takes a target and has an agent build your own version of it, then checks the build against the original.**

Everything below comes from each project's own README, read on 2026-11-09. Both change quickly, so check the sources before relying on a detail. Neither project mentions the other.

## At a glance

|                  | [REA](https://github.com/morluto/rea)                                                 | [Craft Anything](https://github.com/storytold/craft-anything)                                                     |
| ---------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| What you get     | Findings with evidence and limitations; the agent decides what to do with them        | A new project in `app/`, plus checks against the original and the evidence it collected                           |
| Workflow         | Your agent asks, REA inspects and traces, the agent explains, implements and tests    | Study → Build → Check → Ready, repeated until the build is close                                                  |
| Form             | MCP server and CLI (`npx rea-agents setup`)                                           | Desktop app (Simple and Advanced), CLI and MCP server; installers for Windows, macOS, Linux, FreeBSD              |
| Written in       | Node.js                                                                               | Rust                                                                                                              |
| Analysis engines | Uses your Hopper, Ghidra, IDA or Kuna for native code; JavaScript analysis needs none | Own decoders, disassembler and decompiler; uses Ghidra in Deep mode when installed                                |
| Targets          | Native binaries, JavaScript/Electron, .NET, websites, and more                        | Native programs, .NET, Java, Android, Apple, Electron, websites, firmware, packet captures, databases, game files |
| Tool count       | Generated catalog, not committed                                                      | About 320 (302 engine tools in 17 toolsets)                                                                       |
| Agents           | Claude Code, Codex, Cursor, Gemini CLI, Grok Build and others                         | Claude Code first; Copilot, Grok Build and other ACP agents partly verified                                       |
| Default stance   | Evidence-first analysis of what you point it at                                       | Clean room: reads only what a visitor can see; Deep mode reads code and files                                     |
| Maturity         | Frequent releases (v5 went viral in October 2026)                                     | Early alpha, created 2026-10-31                                                                                   |
| License          | MIT                                                                                   | MIT or Apache-2.0                                                                                                 |
| From             | morluto                                                                               | The ArtCraft team, who also publish the [Craft apps](../README.md#the-wider-wave-without-confirmed-rea)           |

## Which one fits

- **You want to understand one feature, protocol or file format**, then write the code yourself or with your agent: REA. It is built for targeted questions and returns evidence your agent can cite. The [rea-lab studies](https://github.com/pablodiazjorge/rea-lab) suggest it pays off most on a known surface, not open-ended exploration.
- **You want a working copy of a website, app or game in a stack you choose**: Craft Anything. The build-and-compare loop is the part REA leaves to your agent.
- **You care about legal exposure**: Craft Anything's default clean-room mode refuses tools that look inside the target. That is a rule about what it offers, not a sandbox, and its README says so. REA has no such mode; what you inspect is up to you. Neither project makes a rebuild legal, see [Legal and controversy](../README.md#legal-and-controversy).
- **You need a GUI**: Craft Anything ships one. For REA, see the community [marrow](https://github.com/utabk/marrow).

## How this list tags them

A case is tagged `REA` only when its source says morluto/rea was used. A project built with Craft Anything is tagged `AI-RE` until enough of them appear to earn their own tag. If you built something with either tool, [submit it](https://github.com/AIshihzong/awesome-reverse-engineer-anything/issues/new?template=case.yml).
