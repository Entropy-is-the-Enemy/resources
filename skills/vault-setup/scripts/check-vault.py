#!/usr/bin/env python3
"""Check a freshly built vault against the vault-setup rules.

Usage:
  python3 check-vault.py "<path to the vault root>"

Reads only; never changes a file. Prints one line per finding. ERROR lines must
be fixed before the build is reported as done; WARNING lines are judgment calls
to fix or explain. Exit code 1 if there is any ERROR, otherwise 0. Needs
Python 3.6 or newer and nothing else.

The checklist (walk it by hand if Python is not available):
  1. Root has _REFERENCE.md, _INDEX.md and CLAUDE.md.
  2. 00 Operating System/ has project-instructions.md, os-spec.md,
     setup-progress.md, Index Refresh/vault-index.py, and the folders Handoffs/,
     Templates/, Reorg Manifests/.
  3. _Inbox/ has _REFERENCE.md and _LOG.md and no _INDEX.md.
  4. memory/, if present, has MEMORY.md and no _INDEX.md.
  5. Archive/ exists.
  6. 00 Operating System/, Archive/ and every numbered folder has
     _REFERENCE.md and _INDEX.md. Any other top-level folder is a leftover
     to raise with the person (WARNING).
  7. Every _INDEX.md has the files:start and files:end marker lines.
  8. Every _REFERENCE.md has Last updated, Recurring files, Purpose and
     State lines (the root needs only Last updated and Purpose).
  9. No template placeholder (<...>) or YYYY-MM-DD is left in a setup file.
 10. No reorg manifest sits at the 00 Operating System/ root.
 11. Setup files follow house style: no em dashes (unless the project
     instructions list that rule under "Dropped defaults:"), no [[wikilinks]].
"""
import os
import re
import sys

OS_FOLDER = "00 Operating System"
NO_INDEX_DIRS = ("_Inbox", "memory")
EM_DASH = chr(0x2014)
# Anything in angle brackets is a candidate; real_placeholders() then drops the
# things Markdown legitimately puts in angle brackets (autolinks, HTML tags).
PLACEHOLDER = re.compile(r"<([^<>\n]{3,})>")
AUTOLINK = re.compile(r"^(?:[a-z][a-z0-9+.-]*:\S+|[^\s@]+@[^\s@]+)$", re.I)
HTML_TAG = re.compile(r"^/?[A-Za-z][A-Za-z0-9]*(?:\s+[A-Za-z-]+\s*=.*)?\s*/?$")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
CODE_SPAN = re.compile(r"`[^`\n]*`")

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except UnicodeDecodeError:
        warn("%s is not UTF-8 text; skipped its content checks" % path)
        return ""


def real_placeholders(prose):
    """Unfilled template slots like <Folder name>, not <https://...>, <a@b.org> or <br>."""
    found = []
    for inner in PLACEHOLDER.findall(prose):
        if AUTOLINK.match(inner) or HTML_TAG.match(inner):
            continue
        found.append("<%s>" % inner)
    return found


def need_file(vault, rel):
    if not os.path.isfile(os.path.join(vault, rel)):
        err("missing file: %s" % rel)
        return False
    return True


def need_dir(vault, rel):
    if not os.path.isdir(os.path.join(vault, rel)):
        err("missing folder: %s/" % rel)
        return False
    return True


def check_reference(vault, rel):
    text = read(os.path.join(vault, rel))
    for label in ("**Last updated:**", "**Recurring files:**", "**Purpose:**", "**State:**"):
        if label not in text:
            # The root reference describes the whole vault; each folder carries its own state.
            if rel == "_REFERENCE.md" and label in ("**State:**", "**Recurring files:**"):
                continue
            err("%s has no %s line" % (rel, label))


def check_index(vault, rel):
    text = read(os.path.join(vault, rel))
    if "<!-- files:start -->" not in text or "<!-- files:end -->" not in text:
        err("%s is missing its files:start / files:end marker lines; recreate it with vault-index.py --create" % rel)


def dropped_defaults(vault):
    """The 'Dropped defaults:' line of the project instructions, lowercased ('' if none)."""
    path = os.path.join(vault, OS_FOLDER, "project-instructions.md")
    if not os.path.isfile(path):
        return ""
    for line in read(path).splitlines():
        if line.strip().lower().startswith("dropped defaults:"):
            return line.lower()
    return ""


def check_style(vault, rel, dropped):
    text = read(os.path.join(vault, rel))
    if EM_DASH in text and "em dash" not in dropped:
        warn("%s contains %d em dash(es); the default rules say use commas, colons or parentheses" % (rel, text.count(EM_DASH)))
    prose = CODE_SPAN.sub("", HTML_COMMENT.sub("", text))
    if "[[" in prose:
        warn("%s contains a [[wikilink]]; the default rules say use backticked paths" % rel)
    # setup-progress.md and os-spec.md legitimately keep some template wording.
    if os.path.basename(rel) not in ("os-spec.md", "setup-progress.md"):
        left = real_placeholders(prose)
        if left:
            err("%s still has template placeholder(s): %s" % (rel, ", ".join(left[:3])))
        if "YYYY-MM-DD" in prose and rel != "CLAUDE.md" and "project-instructions" not in rel:
            err("%s still has an unfilled YYYY-MM-DD date" % rel)


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: python3 check-vault.py "<path to the vault root>"')
    vault = os.path.abspath(sys.argv[1])
    if not os.path.isdir(vault):
        sys.exit("not a folder: %s" % vault)

    setup_files = []

    # 1. Root files
    for rel in ("_REFERENCE.md", "_INDEX.md", "CLAUDE.md"):
        if need_file(vault, rel):
            setup_files.append(rel)

    # 2. Operating system folder
    if need_dir(vault, OS_FOLDER):
        for rel in ("project-instructions.md", "os-spec.md", "setup-progress.md"):
            full = OS_FOLDER + "/" + rel
            if need_file(vault, full):
                setup_files.append(full)
        need_file(vault, OS_FOLDER + "/Index Refresh/vault-index.py")
        for sub in ("Handoffs", "Templates", "Reorg Manifests"):
            need_dir(vault, OS_FOLDER + "/" + sub)
        # 10. Stray manifests
        for name in os.listdir(os.path.join(vault, OS_FOLDER)):
            if name.startswith("reorg-manifest"):
                err("%s/%s sits at the folder root; manifests belong in %s/Reorg Manifests/" % (OS_FOLDER, name, OS_FOLDER))
    if os.path.isfile(os.path.join(vault, "_setup-progress.md")):
        err("_setup-progress.md is still at the vault root; move it to %s/setup-progress.md and log the move" % OS_FOLDER)

    # 3. Inbox
    if need_dir(vault, "_Inbox"):
        if need_file(vault, "_Inbox/_REFERENCE.md"):
            setup_files.append("_Inbox/_REFERENCE.md")
        need_file(vault, "_Inbox/_LOG.md")

    # 4. Memory (optional: the person may have chosen project memory)
    if os.path.isdir(os.path.join(vault, "memory")):
        if need_file(vault, "memory/MEMORY.md"):
            for name in sorted(os.listdir(os.path.join(vault, "memory"))):
                if name.endswith(".md"):
                    setup_files.append("memory/" + name)
    else:
        warn("no memory/ folder; fine only if the person chose Claude project memory in Round F")

    for d in NO_INDEX_DIRS:
        if os.path.isfile(os.path.join(vault, d, "_INDEX.md")):
            err("%s/_INDEX.md exists; %s carries no index" % (d, d))

    # 5. Archive
    need_dir(vault, "Archive")

    # 6 to 8. Every top-level folder
    subject_folders = 0
    for name in sorted(os.listdir(vault)):
        if name.startswith(".") or not os.path.isdir(os.path.join(vault, name)):
            continue
        if name in NO_INDEX_DIRS:
            if name == "_Inbox" and os.path.isfile(os.path.join(vault, "_Inbox/_REFERENCE.md")):
                check_reference(vault, "_Inbox/_REFERENCE.md")
            continue
        if re.match(r"^\d\d ", name) and name != OS_FOLDER:
            subject_folders += 1
        elif name not in (OS_FOLDER, "Archive"):
            warn("top-level folder '%s' is not part of the vault tree; ask the person whether it moves to Archive/ or stays" % name)
            continue
        ref, idx = name + "/_REFERENCE.md", name + "/_INDEX.md"
        if need_file(vault, ref):
            setup_files.append(ref)
            check_reference(vault, ref)
        if need_file(vault, idx):
            check_index(vault, idx)
    if os.path.isfile(os.path.join(vault, "_REFERENCE.md")):
        check_reference(vault, "_REFERENCE.md")
    if os.path.isfile(os.path.join(vault, "_INDEX.md")):
        check_index(vault, "_INDEX.md")
    if subject_folders == 0:
        err("no numbered subject folders found (expected 01 to NN)")
    elif subject_folders > 11:
        warn("%d numbered subject folders; more than 11 is hard to scan (fine if the person approved it)" % subject_folders)

    # 9 and 11. Style and leftovers in the files setup wrote
    dropped = dropped_defaults(vault)
    for rel in setup_files:
        check_style(vault, rel, dropped)

    for msg in errors:
        print("ERROR    " + msg)
    for msg in warnings:
        print("WARNING  " + msg)
    print("summary: %d error(s), %d warning(s), %d setup file(s) checked" % (len(errors), len(warnings), len(setup_files)))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
