#!/usr/bin/env python3
"""Validate the department-copilots marketplace: manifests, skills, commands, references, local-only rules."""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[end + 5:]


def check_plugin(name, path):
    mpath = os.path.join(path, ".claude-plugin", "plugin.json")
    if not os.path.exists(mpath):
        errors.append(f"{name}: missing .claude-plugin/plugin.json"); return
    try:
        m = json.load(open(mpath))
    except Exception as e:
        errors.append(f"{name}: plugin.json invalid JSON: {e}"); return
    if m.get("name") != name:
        errors.append(f"{name}: plugin.json name '{m.get('name')}' != marketplace name")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", m.get("name", "")):
        errors.append(f"{name}: name not kebab-case")
    for k in ("version", "description"):
        if not m.get(k):
            warnings.append(f"{name}: plugin.json missing {k}")
    for bad in ("mcpServers", "hooks"):
        if bad in m or os.path.exists(os.path.join(path, ".mcp.json")) or os.path.isdir(os.path.join(path, "hooks")):
            errors.append(f"{name}: local-only rule - no {bad}/.mcp.json allowed")
    if not os.path.exists(os.path.join(path, "README.md")):
        warnings.append(f"{name}: no README.md")
    # skills
    sdir = os.path.join(path, "skills")
    nskills = 0
    if os.path.isdir(sdir):
        for s in sorted(os.listdir(sdir)):
            sp = os.path.join(sdir, s, "SKILL.md")
            if not os.path.isdir(os.path.join(sdir, s)):
                continue
            if not os.path.exists(sp):
                errors.append(f"{name}: skills/{s} has no SKILL.md"); continue
            nskills += 1
            fm, body = frontmatter(sp)
            if fm is None:
                errors.append(f"{name}: skills/{s}/SKILL.md missing frontmatter"); continue
            if fm.get("name") != s:
                errors.append(f"{name}: skills/{s} frontmatter name '{fm.get('name')}' != dir")
            d = fm.get("description", "")
            if len(d) < 80:
                warnings.append(f"{name}: skills/{s} description short ({len(d)} chars)")
            if "should be used when" not in d:
                warnings.append(f"{name}: skills/{s} description lacks 'should be used when' trigger phrasing")
            lines = body.count("\n")
            if lines > 400:
                warnings.append(f"{name}: skills/{s}/SKILL.md is {lines} lines (>400)")
            for ref in re.findall(r"references/([\w\-.]+\.md)", body):
                if not os.path.exists(os.path.join(sdir, s, "references", ref)):
                    errors.append(f"{name}: skills/{s} references missing file references/{ref}")
            if name not in ("copilot-common", "sticky-notes") and "copilot-common" not in body:
                warnings.append(f"{name}: skills/{s} does not mention copilot-common privacy rules")
    if nskills == 0 and name != "copilot-common":
        errors.append(f"{name}: no skills")
    # commands
    cdir = os.path.join(path, "commands")
    ncmd = 0
    if os.path.isdir(cdir):
        for c in sorted(os.listdir(cdir)):
            if not c.endswith(".md"):
                continue
            ncmd += 1
            fm, body = frontmatter(os.path.join(cdir, c))
            if fm is None or not fm.get("description"):
                errors.append(f"{name}: commands/{c} missing frontmatter description")
            if "$ARGUMENTS" not in body and name != "sticky-notes":
                warnings.append(f"{name}: commands/{c} does not use $ARGUMENTS")
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*\.md", c):
                errors.append(f"{name}: commands/{c} not kebab-case")
    if ncmd == 0 and name != "copilot-common":
        errors.append(f"{name}: no commands")
    # hardcoded home paths
    for dp, _, fs in os.walk(path):
        for f in fs:
            if f.endswith((".md", ".json", ".py")):
                t = open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()
                if "/Users/" in t and "scripts/validate.py" not in f:
                    errors.append(f"{name}: hardcoded /Users/ path in {os.path.relpath(os.path.join(dp, f), path)}")
    return nskills, ncmd


def main():
    mk = json.load(open(os.path.join(ROOT, ".claude-plugin", "marketplace.json")))
    names = [p["name"] for p in mk["plugins"]]
    if len(names) != len(set(names)):
        errors.append("duplicate plugin names in marketplace.json")
    rows = []
    for p in mk["plugins"]:
        src = p["source"]
        if isinstance(src, dict):
            src = os.path.join("plugins", p["name"])  # github source; local checkout is the submodule
        path = os.path.normpath(os.path.join(ROOT, src))
        if not os.path.isdir(path):
            errors.append(f"{p['name']}: source dir {src} missing"); continue
        r = check_plugin(p["name"], path)
        if r:
            rows.append((p["name"], *r))
    listed = {os.path.normpath(os.path.join(ROOT, p["source"] if isinstance(p["source"], str) else os.path.join("plugins", p["name"]))) for p in mk["plugins"]}
    pd = os.path.join(ROOT, "plugins")
    for d in sorted(os.listdir(pd)):
        full = os.path.join(pd, d)
        if os.path.isdir(full) and full not in listed:
            errors.append(f"plugins/{d} exists but is not in marketplace.json")
    print(f"{'plugin':<24}{'skills':>7}{'commands':>10}")
    for n, s, c in rows:
        print(f"{n:<24}{s:>7}{c:>10}")
    print()
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(rows)} plugins checked, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
