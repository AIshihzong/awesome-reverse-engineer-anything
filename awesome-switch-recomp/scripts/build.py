#!/usr/bin/env python3
"""Render the project tables in README.md and README.zh-CN.md from data/projects.json.

Usage:
  python3 scripts/build.py            # rebuild tables from data/
  python3 scripts/build.py --refresh  # also refresh star counts from the GitHub API
                                      # (uses GITHUB_TOKEN if set)
  python3 scripts/build.py --check    # exit 1 if README tables are out of date
"""
import json
import os
import re
import sys
import urllib.request
from datetime import timezone, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.json"
STARS = ROOT / "data" / "stars.json"

DEVICES = ("ios", "mac", "win", "linux", "deck", "android")
STATUSES = ("play", "early", "tool", "-")

LABELS = {
    "en": {
        "head": "| Project | ★ | Game | Runs on | Game version | Status | What it does |\n| --- | ---: | --- | --- | --- | --- | --- |",
        "dev": {"ios": "iPhone/iPad", "mac": "Mac", "win": "Windows", "linux": "Linux", "deck": "Steam Deck", "android": "Android"},
        "st": {"play": "🟢 Playable", "early": "🟡 Early", "tool": "🧰 Tool", "-": "–"},
    },
    "zh": {
        "head": "| 项目 | ★ | 游戏 | 运行设备 | 游戏版本 | 状态 | 说明 |\n| --- | ---: | --- | --- | --- | --- | --- |",
        "dev": {"ios": "iPhone/iPad", "mac": "Mac", "win": "Windows", "linux": "Linux", "deck": "Steam Deck", "android": "Android"},
        "st": {"play": "🟢 可玩", "early": "🟡 早期", "tool": "🧰 工具", "-": "–"},
    },
}


def fmt_stars(n):
    if n is None:
        return "–"
    if n >= 10000:
        return f"{n / 1000:.1f}k"
    return f"{n:,}"


def load():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    stars = json.loads(STARS.read_text(encoding="utf-8")) if STARS.exists() else {"stars": {}}
    return data, stars


def refresh_stars(data, stars):
    token = os.environ.get("GITHUB_TOKEN")
    for p in data["projects"]:
        req = urllib.request.Request(f"https://api.github.com/repos/{p['repo']}")
        req.add_header("Accept", "application/vnd.github+json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                info = json.load(r)
            stars["stars"][p["repo"]] = info["stargazers_count"]
            if info.get("full_name") and info["full_name"] != p["repo"]:
                print(f"note: {p['repo']} moved to {info['full_name']}", file=sys.stderr)
            if info.get("archived"):
                print(f"note: {p['repo']} is archived", file=sys.stderr)
        except Exception as e:  # keep the old number on errors
            print(f"warn: {p['repo']}: {e}", file=sys.stderr)
    stars["updated"] = datetime.now(timezone.utc).date().isoformat()
    STARS.write_text(json.dumps(stars, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def cell(s):
    return s.replace("|", "\\|")


def render_section(sec, projects, stars, lang):
    L = LABELS[lang]
    rows = [p for p in projects if p["s"] == sec["id"]]
    rows.sort(key=lambda p: -(stars["stars"].get(p["repo"]) or 0))
    out = []
    intro = sec.get(f"intro_{lang}")
    if intro:
        out.append(intro)
        out.append("")
    link = lambda p: f"[{p['name']}](https://github.com/{p['repo']})"
    if sec.get("bullets") or "dev" not in rows[0]:
        for p in rows:
            out.append(f"- {link(p)} ({fmt_stars(stars['stars'].get(p['repo']))} ★): {p[lang]}")
        return "\n".join(out)
    out.append(L["head"])
    for p in rows:
        name = link(p) + (" 🤖" if p.get("agent") else "")
        dev = ", ".join(L["dev"][d] for d in sorted(p["dev"].split(","), key=DEVICES.index))
        out.append(
            f"| {name} | {fmt_stars(stars['stars'].get(p['repo']))} | {cell(p['game_' + lang])} | {dev} | {cell(p['ver'])} | {L['st'][p['st']]} | {cell(p[lang])} |"
        )
    return "\n".join(out)


def render_file(path, data, stars, lang):
    text = path.read_text(encoding="utf-8")
    for sec in data["sections"]:
        body = render_section(sec, data["projects"], stars, lang)
        pat = re.compile(rf"(<!-- BEGIN {sec['id']} -->\n).*?(<!-- END {sec['id']} -->)", re.S)
        if not pat.search(text):
            sys.exit(f"{path.name}: missing markers for {sec['id']}")
        text = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)
    count = sum(1 for p in data["projects"] if "dev" in p)
    text = re.sub(r"<!-- COUNT -->\d+<!-- /COUNT -->", f"<!-- COUNT -->{count}<!-- /COUNT -->", text)
    text = re.sub(r"<!-- DATE -->[\d-]+<!-- /DATE -->", f"<!-- DATE -->{stars.get('updated', data['checked'])}<!-- /DATE -->", text)
    return text


def validate(data):
    repos = [p["repo"] for p in data["projects"]]
    dupes = {r for r in repos if repos.count(r) > 1}
    if dupes:
        sys.exit(f"duplicate entries: {sorted(dupes)}")
    ids = {s["id"] for s in data["sections"]}
    for p in data["projects"]:
        if p["s"] not in ids:
            sys.exit(f"{p['repo']}: unknown section {p['s']}")
        for k in ("repo", "name", "en", "zh"):
            if not p.get(k):
                sys.exit(f"{p.get('repo')}: missing {k}")
        if "dev" in p:
            for d in p["dev"].split(","):
                if d not in DEVICES:
                    sys.exit(f"{p['repo']}: unknown device {d}")
            if p["st"] not in STATUSES:
                sys.exit(f"{p['repo']}: unknown status {p['st']}")
            for k in ("game_en", "game_zh", "ver"):
                if not p.get(k):
                    sys.exit(f"{p['repo']}: missing {k}")


def main():
    data, stars = load()
    validate(data)
    if "--refresh" in sys.argv:
        refresh_stars(data, stars)
    stale = False
    for name, lang in (("README.md", "en"), ("README.zh-CN.md", "zh")):
        path = ROOT / name
        new = render_file(path, data, stars, lang)
        if new != path.read_text(encoding="utf-8"):
            stale = True
            if "--check" not in sys.argv:
                path.write_text(new, encoding="utf-8")
    if "--check" in sys.argv and stale:
        sys.exit("README tables are out of date: run python3 scripts/build.py")


if __name__ == "__main__":
    main()
