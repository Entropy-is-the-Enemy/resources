#!/usr/bin/env python3
"""Vault index refresh.

Rewrites the generated block of every _INDEX.md in the vault, between
<!-- files:start --> and <!-- files:end -->. Text outside the markers is never
touched. Needs Python 3.6 or newer and nothing else.

This file must sit at: <vault>/00 Operating System/Index Refresh/vault-index.py
The vault root is found from that location, so the script runs from anywhere.

Usage:
  python3 vault-index.py                    refresh every stale index
  python3 vault-index.py --check            report stale indexes, write nothing (exit 1 if any)
  python3 vault-index.py --path "04 Reports"   limit to one subtree
  python3 vault-index.py --create "04 Reports/Monthly"   add a new _INDEX.md to a folder
  python3 vault-index.py --create .         add the root _INDEX.md

Rules:
  - memory/ and _Inbox/ carry no index; this script never creates one there.
    (_Inbox is a transit folder and memory has its own MEMORY.md index.)
  - Listing: subfolders first, then files, each in plain byte order, folders
    with a trailing slash, every name in backticks (plain Markdown, no wikilinks).
  - Left out: _INDEX.md itself, dotfiles, Office lock files (~$...), and the
    operating-system files named in CRUFT.
"""
import argparse
import os
import sys

START = "<!-- files:start -->"
END = "<!-- files:end -->"
STAMP = "<!-- Written by 00 Operating System/Index Refresh/vault-index.py. Do not edit by hand; rerun the script. -->"
NO_INDEX_DIRS = {"memory", "_Inbox"}
CRUFT = {"desktop.ini", "Thumbs.db", ".DS_Store", "__pycache__"}
OS_FOLDER = "00 Operating System"

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def listing(folder):
    dirs, files = [], []
    for name in os.listdir(folder):
        if name == "_INDEX.md" or name.startswith(".") or name.startswith("~$") or name in CRUFT:
            continue
        (dirs if os.path.isdir(os.path.join(folder, name)) else files).append(name)
    key = lambda n: n.encode("utf-8")
    return ["- `%s/`" % d for d in sorted(dirs, key=key)] + ["- `%s`" % f for f in sorted(files, key=key)]


def block(folder):
    return "\n".join([START, STAMP, ""] + listing(folder) + ["", END])


def refresh(path, write):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if START not in text or END not in text or text.index(END) < text.index(START):
        return "no-markers"
    a = text.index(START)
    b = text.index(END, a) + len(END)
    new = text[:a] + block(os.path.dirname(path)) + text[b:]
    if new == text:
        return "current"
    if write:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
    return "updated" if write else "stale"


def excluded(rel):
    return rel.replace("\\", "/").split("/")[0] in NO_INDEX_DIRS


def show(rel):
    return "(root)" if rel == "." else rel.replace("\\", "/")


def create(arg):
    folder = os.path.normpath(os.path.join(VAULT, arg))
    rel = os.path.relpath(folder, VAULT)
    if rel.startswith(".."):
        sys.exit("refused: %s is outside the vault" % arg)
    if not os.path.isdir(folder):
        sys.exit("not a folder: %s (create the folder first, then run --create)" % show(rel))
    if excluded(rel):
        sys.exit("refused: %s carries no index by rule" % show(rel))
    target = os.path.join(folder, "_INDEX.md")
    if os.path.exists(target):
        sys.exit("already exists: %s/_INDEX.md (run without --create to refresh it)" % show(rel))
    title = os.path.basename(folder) if rel != "." else os.path.basename(VAULT)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# %s: index\n\n%s\n" % (title, block(folder)))
    print("created  %s/_INDEX.md" % show(rel))


def main():
    ap = argparse.ArgumentParser(description="Refresh the _INDEX.md files in this vault.")
    ap.add_argument("--check", action="store_true", help="report only; exit 1 if any index is stale")
    ap.add_argument("--path", default="", help="subtree relative to the vault root")
    ap.add_argument("--create", default="", help="folder (relative to the vault root) to give a new _INDEX.md; use . for the root")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(VAULT, OS_FOLDER)):
        sys.exit(
            "cannot find the vault: this script must sit at "
            "<vault>/%s/Index Refresh/vault-index.py, but %s has no '%s' folder" % (OS_FOLDER, VAULT, OS_FOLDER)
        )

    if args.create:
        create(args.create)
        return

    root = os.path.normpath(os.path.join(VAULT, args.path))
    # Same guard as --create: an absolute path or ".." must not reach indexes outside the vault.
    if os.path.relpath(root, VAULT).startswith(".."):
        sys.exit("refused: %s is outside the vault" % args.path)
    if not os.path.isdir(root):
        sys.exit("not a folder: %s" % args.path)
    counts = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in CRUFT)
        rel = os.path.relpath(dirpath, VAULT)
        if rel != "." and excluded(rel):
            dirnames[:] = []
            continue
        if "_INDEX.md" not in filenames:
            continue
        status = refresh(os.path.join(dirpath, "_INDEX.md"), write=not args.check)
        counts[status] = counts.get(status, 0) + 1
        if status != "current":
            print("%-11s%s/_INDEX.md" % (status, show(rel)))
    if not counts:
        print("summary: no _INDEX.md files found (create one with --create \"<folder>\")")
    else:
        print("summary: " + ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())))
    if counts.get("no-markers"):
        print("note: a 'no-markers' index is missing its files:start / files:end lines; add them and rerun")
    if args.check and (counts.get("stale") or counts.get("no-markers")):
        sys.exit(1)


if __name__ == "__main__":
    main()
