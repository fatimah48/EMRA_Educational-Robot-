# organize_interfaces.py
# Renames and crops the raw EMRA screen captures into the docs/interfaces tree
# and regenerates the gallery README that the thesis points at.
#
# Run it again every time you add new captures. It rebuilds the tree from
# scratch, so the manifest is the single source of truth.

# ---------------------------------------------------------------- settings --
RAW_DIR = "raw_screenshots"          # folder holding the original grim captures
MANIFEST = "interfaces_manifest.csv"  # mapping file
OUT_DIR = "docs/interfaces"
README_OUT = "README.md"
HEADER = "README_header.md"
COLUMNS = 2
HOLD_DIR = "_privacy_review"          # captures held back until anonymised
REPO_URL = "https://github.com/USERNAME/EMRA"  # used in the README header

INTROS = "module_intros.md"           # prose shown above each gallery section

CHEST_BOX = (1080, 0, 2848, 828)      # chest touchscreen region, the only one used

MODULE_TITLES = {
    "00-overview": "Overview and session start",
    "01-talk": "Talk with EMRA",
    "02-body-parts": "Body parts",
    "03-puzzle": "Puzzle",
    "04-lego": "LEGO build",
    "05-painting": "Painting",
    "06-colors": "Colours",
    "07-numbers": "Numbers",
    "08-writing": "Writing",
    "09-reading": "Reading",
    "10-letters": "Letters",
    "11-educator-dashboard": "Educator dashboard",
    "12-admin": "Administrator panel",
}
# ---------------------------------------------------------------------------

import csv
import io
import os
import shutil
from PIL import Image


def target_name(row):
    parts = [row["order"], row["slug"]]
    if row["lang"] and row["lang"] not in ("xx", ""):
        parts.append(row["lang"])
    return "-".join(parts) + ".png"


def crop_for(img, kind):
    if kind == "full":
        return img
    return img.crop(CHEST_BOX)


def read_intros():
    intros = {}
    if not os.path.isfile(INTROS):
        return intros
    key = None
    buf = []
    with open(INTROS, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## "):
                if key:
                    intros[key] = "\n".join(buf).strip()
                key = line[3:].strip()
                buf = []
            elif key:
                buf.append(line.rstrip())
    if key:
        intros[key] = "\n".join(buf).strip()
    return intros


def main():
    rows = []
    with open(MANIFEST, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["source"].strip():
                rows.append(row)

    for path in (OUT_DIR, HOLD_DIR):
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.makedirs(path)

    published = {}
    held = []
    missing = []

    for row in rows:
        src = os.path.join(RAW_DIR, row["source"])
        if not os.path.isfile(src):
            missing.append(row["source"])
            continue
        if row["privacy"] == "skip":
            continue
        base = OUT_DIR if row["privacy"] == "ok" else HOLD_DIR
        folder = os.path.join(base, row["module"])
        if not os.path.isdir(folder):
            os.makedirs(folder)
        name = target_name(row)
        img = Image.open(src)
        crop_for(img, row["crop"]).save(os.path.join(folder, name), optimize=True)
        record = (name, row["caption"], row["module"])
        if row["privacy"] == "ok":
            published.setdefault(row["module"], []).append(record)
        else:
            held.append(os.path.join(row["module"], name))

    write_readme(published, held, read_intros())

    print("published: " + str(sum(len(v) for v in published.values())))
    print("held for anonymisation: " + str(len(held)))
    for item in held:
        print("  " + item)
    if missing:
        print("missing source files: " + str(len(missing)))
        for item in missing:
            print("  " + item)


def write_readme(published, held, intros):
    lines = []
    if os.path.isfile(HEADER):
        with io.open(HEADER, encoding="utf-8") as fh:
            lines.append(fh.read().rstrip())
        lines.append("")
    for module in sorted(MODULE_TITLES):
        items = sorted(published.get(module, []))
        lines.append("## " + MODULE_TITLES[module])
        lines.append("")
        if module in intros:
            lines.append(intros[module])
            lines.append("")
        if not items:
            lines.append("_Screens for this activity are being captured._")
            lines.append("")
            continue
        lines.append("<table>")
        for i in range(0, len(items), COLUMNS):
            row = items[i:i + COLUMNS]
            lines.append("<tr>")
            for name, caption, mod in row:
                src = OUT_DIR + "/" + mod + "/" + name
                cell = '<td width="' + str(int(100 / COLUMNS)) + '%">'
                cell += '<img src="' + src + '" width="100%"><br>'
                cell += "<sub>" + caption + "</sub></td>"
                lines.append(cell)
            for _ in range(COLUMNS - len(row)):
                lines.append("<td></td>")
            lines.append("</tr>")
        lines.append("</table>")
        lines.append("")
    with io.open(README_OUT, "w", encoding="utf-8") as fh:
        fh.write(chr(10).join(lines).rstrip() + chr(10))


if __name__ == "__main__":
    main()
