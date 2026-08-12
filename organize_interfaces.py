# organize_interfaces.py
# Renames and crops the raw EMRA screen captures into the docs/interfaces tree
# and regenerates the gallery README that the thesis points at.
#
# Run it again every time you add new captures. It rebuilds the tree from
# scratch, so the manifest is the single source of truth.

# ---------------------------------------------------------------- settings --
RAW_DIR = "raw_screenshots"          # folder holding the original grim captures
MANIFEST = "interfaces_manifest.csv"  # mapping file
OUT_DIR = "docs/interfaces"           # published gallery
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
    lines.append("# EMRA interface gallery")
    lines.append("")
    lines.append("Screen captures of the deployed EMRA system, taken from the 1768x828")
    lines.append("chest touchscreen. Sections follow the order the activities appear in on")
    lines.append("the main menu. Each section opens with a description of what the")
    lines.append("activity asks the child to do and how the response is judged, followed")
    lines.append("by the captures for that activity in both languages.")
    lines.append("")
    lines.append("Cite this gallery from the thesis by module and file name, for example")
    lines.append("`03-puzzle/03-gameplay-bus-en.png`.")
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for module in sorted(MODULE_TITLES):
        title = MODULE_TITLES[module]
        count = len(published.get(module, []))
        state = str(count) + (" figure" if count == 1 else " figures")
        if not count:
            state = "pending capture"
        lines.append("- [" + title + "](#" + module + ") (" + state + ")")
    lines.append("")
    for module in sorted(MODULE_TITLES):
        lines.append('<a id="' + module + '"></a>')
        lines.append("")
        lines.append("## " + MODULE_TITLES[module])
        lines.append("")
        if module in intros:
            lines.append(intros[module])
            lines.append("")
        items = published.get(module, [])
        if not items:
            lines.append("_Captures pending._")
            lines.append("")
            continue
        for name, caption, mod in sorted(items):
            lines.append("**`" + mod + "/" + name + "`** " + caption)
            lines.append("")
            lines.append('<img src="' + mod + "/" + name + '" width="700">')
            lines.append("")
    if held:
        lines.append("## Withheld")
        lines.append("")
        lines.append(str(len(held)) + " captures show real participant names, identifiers")
        lines.append("or e-mail addresses and are held out of this repository until they are")
        lines.append("recaptured with synthetic data.")
        lines.append("")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
