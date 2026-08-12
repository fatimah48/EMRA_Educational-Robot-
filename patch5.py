import csv, io

ADD = [["20260811_15h32m45s_grim.png","10-letters","00","menu","en",
        "Entry screen for the two letter activities, the recognition garden and tracing.","ok","chest"]]
RESTORE = [("06-colors","05")]

rows = list(csv.reader(io.open("interfaces_manifest.csv", encoding="utf-8")))
have = set((r[1], r[2]) for r in rows[1:])
for r in rows[1:]:
    if (r[1], r[2]) in RESTORE:
        r[6] = "ok"
for a in ADD:
    if (a[1], a[2]) not in have:
        rows.append(a)
with io.open("interfaces_manifest.csv", "w", encoding="utf-8", newline="") as fh:
    csv.writer(fh).writerows(rows)
print("done")
