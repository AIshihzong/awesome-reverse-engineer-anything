# What is REA (Reverse Engineer Anything)? FAQ

**English** · [简体中文](what-is-rea.zh-CN.md) · [Back to the list](../README.md)

> ⭐ [Star the list on GitHub](https://github.com/AIshihzong/awesome-reverse-engineer-anything) to find it again, or **Watch → Custom → Releases** for the [weekly digest](https://github.com/AIshihzong/awesome-reverse-engineer-anything/releases).

Short answers to the questions people ask most about REA, with links to the sources. Facts were checked for the main list; star counts and versions change weekly, so read the date next to a number.

## What is REA?

REA, short for **Reverse Engineer Anything**, is [morluto/rea](https://github.com/morluto/rea): an open-source (MIT) MCP server and CLI that lets coding agents inspect native binaries, Electron apps, .NET assemblies, Android APKs, firmware and websites without their source code, explain how a feature works with evidence, and rebuild it. It had 417k+ GitHub stars as of 2026-11-01.

## Does REA decompile programs itself?

No. REA orchestrates existing tools such as Hopper, Ghidra, IDA and JADX for the agent, and gathers their results as evidence.

## How do I install REA?

The published package is [`rea-agents` on npm](https://www.npmjs.com/package/rea-agents). Run `npx rea-agents setup` to register it with your agent. The official docs are on [rea.tools](https://rea.tools/), with [illustrated guides](https://rea.tools/guides/), and there is a [Chinese README](https://github.com/morluto/rea/blob/main/docs/readme/README_zh.md).

## Where do I get REA safely?

Only from [morluto/rea](https://github.com/morluto/rea), [rea.tools](https://rea.tools/) and the npm package `rea-agents`. Some GitHub repositories with similar names offer an "official free download" as zip files. They are not official. Do not run archives or executables from anywhere else.

## Is REA safe to run on my machine?

Analysis runs locally, but tool results pass through the agent to your model provider. REA's own SECURITY.md says REA is not a sandbox. Commercial tools it can drive, such as IDA Pro, Hopper and JEB, must be licensed separately; REA provides no licenses.

## Is it legal to use REA?

Reverse engineering is governed by local law, software licenses and terms of service. REA's [DISCLAIMER.md](https://github.com/morluto/rea/blob/main/DISCLAIMER.md) lists permitted uses: learning, research, interoperability, preservation, security research, vulnerability disclosure and CTFs. It excludes copying proprietary software or reproducing its protected code and assets. More in [Legal and controversy](../README.md#legal-and-controversy).

## What has REA been used for? Examples

The official [showcases](https://rea.tools/showcase/) include a byte-exact rebuild of one DX-Ball sound function, tracing Notion's Electron clipboard bridge, and tracing TOTP code generation in the Aegis Android app. Community projects that say they used REA include [hexgrab](https://github.com/iammukeshm/hexgrab), a .NET colour picker, and [rec-rs](https://github.com/michaelshimeles/rec-rs), a Rust screen recorder for macOS. See [all community cases](../README.md#community-cases-built-with-rea) and the [index by app](by-app.md).

## Did the viral demos really use REA?

Often not. Of the six [most-shared cases](../README.md#most-shared), only DX-Ball says in its own repo that it used REA. Two more say so only in the author's post, and the other three used other tools or are unverified. [Did it really use REA?](is-it-rea.md) checks each claim against its source.

## Can REA clone a whole app or recover its source code?

The official project does not claim either. The DX-Ball figures (3,205 matching test cases, 63 matching bytes) apply to one function, not the whole game.

## Does REA actually help agents?

The controlled tests we know of are mixed. [rea-lab](https://github.com/pablodiazjorge/rea-lab) ran 482 Claude Code runs and found no significant gain in solve rate, with REA runs taking about twice the time and cost. [leanrea](https://github.com/aicodeking/leanrea) found a plain-CLI skill came close to REA's accuracy at lower cost. Details in [Does REA help? The evidence](../README.md#does-rea-help-the-evidence).

## REA or Craft Anything?

REA explains how a program works and shows the evidence. Craft Anything has an agent build your own version of a target and checks the build against the original. See [REA or Craft Anything?](rea-vs-craft-anything.md)

## Where can I ask questions about REA?

On the official [Discord](https://discord.gg/GkcryMnJDM) (Q&A and Show and Tell) and in [GitHub Discussions](https://github.com/morluto/rea/discussions). This FAQ and list are unofficial and not affiliated with morluto/rea.
