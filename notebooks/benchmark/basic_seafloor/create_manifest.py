"""Discover 100 consecutive Hake RAW files"""
import csv
from pathlib import Path

import s3fs

BUCKET = "noaa-wcsd-pds"
PREFIX = f"{BUCKET}/data/raw/Bell_M._Shimada/SH2306/EK80"
ANCHOR = f"{PREFIX}/Hake-D20230811-T165727.raw"
ANCHOR_SHA256 = "dcc69f8a0cacc54a76ce3b598194bfb78b4580eb535ca19daf5b17e266ea5e52"
COUNT = 100

fs = s3fs.S3FileSystem(anon=True)
keys = sorted(fs.glob(f"{PREFIX}/Hake-D*.raw"))
start = keys.index(ANCHOR)
keys = keys[start : start + COUNT]
if len(keys) != COUNT:
    raise ValueError(f"Expected {COUNT} files, found {len(keys)}")

output = Path(__file__).with_name("manifest.csv")
with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["url", "sha256"])
    writer.writeheader()
    for key in keys:
        writer.writerow({
            "url": f"https://{BUCKET}.s3.amazonaws.com/{key.split('/', 1)[1]}",
            "sha256": ANCHOR_SHA256 if key == ANCHOR else "",
        })
print(f"Wrote {len(keys)} files to {output}")
