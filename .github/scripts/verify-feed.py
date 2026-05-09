#!/usr/bin/env python3
"""Fail if public/feeds/index.rss2 is missing, malformed, or empty."""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

feed = Path("public/feeds/index.rss2")
if not feed.is_file() or feed.stat().st_size == 0:
    sys.exit(f"::error::{feed} is missing or empty")

root = ET.parse(feed).getroot()
if root.tag != "rss":
    sys.exit(f"::error::{feed} root is <{root.tag}>, expected <rss>")

items = root.findall("./channel/item")
print(f"RSS items: {len(items)}")
if not items:
    sys.exit(f"::error::{feed} has no <item> entries")
