#!/usr/bin/env python3
"""Sticky Notes: local Markdown notes with tags, topics and action items.

Storage: $COPILOT_NOTES_DIR or ~/.copilots/sticky-notes/<YYYY-MM-DD>-<slug>.md
Each note is a Markdown file with a small YAML-ish header:

    ---
    id: 20261006-1412-ont-rx
    created: 2026-10-06T14:12:05
    topic: ticket-48812
    tags: noc, optical
    ---
    body text ...
    - [ ] action item
    - [x] done action

Commands:
  add    "text" [--topic T] [--tags a,b] [--title TITLE]
  list   [--topic T] [--tag X] [--days N] [--limit N]
  search "query" [--topic T]
  actions [--topic T] [--all]        open (or all) checkbox items across notes
  done   NOTE_ID N                   tick the Nth open action in a note
  bundle TOPIC|"query" [--days N]    assemble a context bundle (notes + open actions)
  topics                             list topics with note counts
  path                               print storage directory
Stdlib only. Never leaves the machine.
"""
import argparse
import datetime as dt
import os
import re
import sys

HOME = os.path.expanduser("~")
DIR = os.environ.get("COPILOT_NOTES_DIR") or os.path.join(HOME, ".copilots", "sticky-notes")
CHECK = re.compile(r"^(\s*[-*]\s*)\[( |x|X)\]\s*(.*)$")


def ensure_dir():
    os.makedirs(DIR, exist_ok=True)


def slug(s, n=40):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n] or "note"


def parse(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = text[end + 5:]
    meta.setdefault("id", os.path.splitext(os.path.basename(path))[0])
    meta.setdefault("topic", "")
    meta.setdefault("tags", "")
    meta.setdefault("created", dt.datetime.fromtimestamp(os.path.getmtime(path)).isoformat(timespec="seconds"))
    return {"path": path, "meta": meta, "body": body, "tags": [t.strip() for t in meta["tags"].split(",") if t.strip()]}


def all_notes():
    ensure_dir()
    notes = [parse(os.path.join(DIR, f)) for f in os.listdir(DIR) if f.endswith(".md")]
    return sorted(notes, key=lambda n: n["meta"]["created"], reverse=True)


def within_days(note, days):
    if not days:
        return True
    try:
        created = dt.datetime.fromisoformat(note["meta"]["created"])
    except ValueError:
        return True
    return created >= dt.datetime.now() - dt.timedelta(days=days)


def actions_of(note):
    out = []
    for i, line in enumerate(note["body"].splitlines()):
        m = CHECK.match(line)
        if m:
            out.append({"line": i, "done": m.group(2).lower() == "x", "text": m.group(3).strip()})
    return out


def cmd_add(a):
    ensure_dir()
    now = dt.datetime.now()
    title = a.title or a.text.strip().splitlines()[0][:60]
    nid = now.strftime("%Y%m%d-%H%M") + "-" + slug(title, 30)
    path = os.path.join(DIR, nid + ".md")
    i = 1
    while os.path.exists(path):
        i += 1
        path = os.path.join(DIR, f"{nid}-{i}.md")
    heading = f"# {a.title}\n\n" if a.title else ""
    content = (
        "---\n"
        f"id: {os.path.splitext(os.path.basename(path))[0]}\n"
        f"created: {now.isoformat(timespec='seconds')}\n"
        f"topic: {a.topic or ''}\n"
        f"tags: {a.tags or ''}\n"
        "---\n"
        f"{heading}{a.text.strip()}\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"saved {path}")


def fmt_note(n, full=False):
    m = n["meta"]
    head = f"[{m['id']}] {m['created'][:16].replace('T', ' ')}"
    if m["topic"]:
        head += f"  topic={m['topic']}"
    if n["tags"]:
        head += "  tags=" + ",".join(n["tags"])
    acts = actions_of(n)
    open_n = sum(1 for x in acts if not x["done"])
    if open_n:
        head += f"  open-actions={open_n}"
    first = next((l for l in n["body"].splitlines() if l.strip() and not l.startswith("#")), "")
    if full:
        return head + "\n" + n["body"].rstrip() + "\n"
    return head + "\n    " + first[:120]


def filt(notes, a):
    out = []
    for n in notes:
        if getattr(a, "topic", None) and n["meta"]["topic"].lower() != a.topic.lower():
            continue
        if getattr(a, "tag", None) and a.tag.lower() not in [t.lower() for t in n["tags"]]:
            continue
        if not within_days(n, getattr(a, "days", 0)):
            continue
        out.append(n)
    return out


def cmd_list(a):
    notes = filt(all_notes(), a)[: a.limit]
    if not notes:
        print("no notes")
    for n in notes:
        print(fmt_note(n))


def score(n, terms):
    hay = (n["body"] + " " + n["meta"]["topic"] + " " + " ".join(n["tags"])).lower()
    return sum(hay.count(t) for t in terms)


def cmd_search(a):
    terms = [t for t in a.query.lower().split() if t]
    notes = [(score(n, terms), n) for n in filt(all_notes(), a)]
    notes = [x for x in notes if x[0] > 0]
    notes.sort(key=lambda x: (-x[0], x[1]["meta"]["created"]), reverse=False)
    if not notes:
        print("no matches")
    for s, n in notes[: a.limit]:
        print(fmt_note(n))
        for line in n["body"].splitlines():
            if any(t in line.lower() for t in terms):
                print("    > " + line.strip()[:140])


def cmd_actions(a):
    found = False
    for n in filt(all_notes(), a):
        acts = [x for x in actions_of(n) if a.all or not x["done"]]
        if not acts:
            continue
        found = True
        print(f"[{n['meta']['id']}]" + (f" topic={n['meta']['topic']}" if n["meta"]["topic"] else ""))
        k = 0
        for x in actions_of(n):
            if x["done"] and not a.all:
                continue
            k += 1
            mark = "x" if x["done"] else " "
            print(f"  {k}. [{mark}] {x['text']}")
    if not found:
        print("no open actions")


def cmd_done(a):
    path = os.path.join(DIR, a.note_id + ".md")
    if not os.path.exists(path):
        sys.exit(f"no note {a.note_id}")
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    k = 0
    for i, line in enumerate(lines):
        m = CHECK.match(line)
        if m and m.group(2) == " ":
            k += 1
            if k == a.n:
                lines[i] = f"{m.group(1)}[x] {m.group(3)}"
                with open(path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
                print(f"done: {m.group(3)}")
                return
    sys.exit(f"note {a.note_id} has no open action #{a.n}")


def cmd_bundle(a):
    notes = all_notes()
    by_topic = [n for n in notes if n["meta"]["topic"].lower() == a.key.lower()]
    terms = [t for t in a.key.lower().split() if t]
    by_search = [n for n in notes if n not in by_topic and score(n, terms) > 0]
    chosen = [n for n in by_topic + by_search if within_days(n, a.days)]
    print(f"CONTEXT BUNDLE: {a.key}  ({len(chosen)} notes, newest first)\n")
    if not chosen:
        print("no matching notes")
        return
    open_acts = []
    for n in chosen:
        print("=" * 60)
        print(fmt_note(n, full=True))
        for x in actions_of(n):
            if not x["done"]:
                open_acts.append((n["meta"]["id"], x["text"]))
    print("=" * 60)
    print("\nOPEN ACTIONS")
    if not open_acts:
        print("  none")
    for nid, t in open_acts:
        print(f"  - {t}   ({nid})")


def cmd_topics(a):
    counts = {}
    for n in all_notes():
        t = n["meta"]["topic"] or "(none)"
        counts[t] = counts.get(t, 0) + 1
    for t, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{c:4}  {t}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("add"); p.add_argument("text"); p.add_argument("--topic"); p.add_argument("--tags"); p.add_argument("--title"); p.set_defaults(fn=cmd_add)
    p = sp.add_parser("list"); p.add_argument("--topic"); p.add_argument("--tag"); p.add_argument("--days", type=int, default=0); p.add_argument("--limit", type=int, default=30); p.set_defaults(fn=cmd_list)
    p = sp.add_parser("search"); p.add_argument("query"); p.add_argument("--topic"); p.add_argument("--tag"); p.add_argument("--days", type=int, default=0); p.add_argument("--limit", type=int, default=20); p.set_defaults(fn=cmd_search)
    p = sp.add_parser("actions"); p.add_argument("--topic"); p.add_argument("--tag"); p.add_argument("--days", type=int, default=0); p.add_argument("--all", action="store_true"); p.set_defaults(fn=cmd_actions)
    p = sp.add_parser("done"); p.add_argument("note_id"); p.add_argument("n", type=int); p.set_defaults(fn=cmd_done)
    p = sp.add_parser("bundle"); p.add_argument("key"); p.add_argument("--days", type=int, default=0); p.set_defaults(fn=cmd_bundle)
    p = sp.add_parser("topics"); p.set_defaults(fn=cmd_topics)
    p = sp.add_parser("path"); p.set_defaults(fn=lambda a: print(DIR))
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
