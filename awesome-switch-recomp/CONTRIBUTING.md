# Contributing / 参与贡献

Thanks for helping. The fastest way is to [open an issue](https://github.com/AIshihzong/awesome-switch-recomp/issues/new?template=project.yml) with the repository link; a maintainer will read its README and add it.

## What gets in

- Open source, with the code on GitHub, GitLab or Codeberg.
- It recompiles or natively ports a Nintendo Switch or Switch 2 game, or it is a tool that builds such ports.
- Its README says the player must bring their own copy of the game.
- Not accepted: projects that include, or link to, games, keys, firmware or pre-built games; download sites; emulators; closed-source tools.

## Sending a pull request

1. Add one object to `projects` in [`data/projects.json`](data/projects.json): `s` (section id: `apple`, `pc`, `android`, `tools`), `repo`, `name`, `game_en`, `game_zh`, `dev` (comma-separated: `ios`, `mac`, `win`, `linux`, `deck`, `android`), `ver` (the supported game version, or `–`), `st` (`play`, `early`, `tool`, or `-` if the README doesn't say), `agent` (true if the README says it was written mostly with an AI agent), and a one-line `en` and `zh` description.
2. Base the version and status on the project's README, and say where in your PR description.
3. Run `python3 scripts/build.py` to regenerate both READMEs. Do not edit the tables by hand; CI checks they match the data.
4. Keep descriptions factual: what it runs, on what, and how far it gets. No "best" or "ultimate".

中文贡献者：流程相同。描述请同时写 `en` 和 `zh`，中文用自然的说法，不要机翻。

## Corrections and takedowns

If a project changes (a new supported version, now playable, moved, archived), open an issue with a link to the line in its README. If you hold rights to a game and want an entry removed, open an issue: it is removed without discussion.
