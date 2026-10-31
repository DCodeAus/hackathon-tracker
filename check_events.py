"""
Checks events.json - run by GitHub on every push and once a week (see
.github/workflows/check-events.yml), or by hand:

    python3 check_events.py

Problems that would break the site (invalid JSON, a missing title or a
date it can't sort by, a repeated id) fail the check. Things that just
need attention are warnings:

  - an upcoming event whose date is still "TBA"
  - an upcoming event with no link, or any link that isn't a full
    https:// address
  - fewer than MIN_UPCOMING upcoming events - time to look through
    SOURCES.md for more

On the weekly run, too few upcoming events fails the check too, so GitHub
emails you about it rather than leaving a warning nobody sees.
"""

import datetime
import json
import os
import re
import sys

MIN_UPCOMING = 5
REQUIRED = ["id", "title", "date", "sortDate", "location", "description", "link", "tags"]

# GitHub turns lines starting "::error" / "::warning" into notes on the run.
errors = []
warnings = []

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "events.json"), encoding="utf-8") as f:
        events = json.load(f)
except ValueError as e:
    print(f"::error file=events.json::events.json isn't valid JSON - {e}")
    sys.exit(1)

today = datetime.date.today().isoformat()
seen_ids = set()
upcoming = []

for event in events:
    name = event.get("title") or f"event id {event.get('id')}"
    missing = [field for field in REQUIRED if field not in event]
    if missing:
        errors.append(f"'{name}' is missing {', '.join(missing)}")
    if event.get("id") in seen_ids:
        errors.append(f"id {event.get('id')} is used more than once")
    seen_ids.add(event.get("id"))

    dates = [event.get("sortDate"), event.get("endDate")]
    if any(d is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(d)) for d in dates):
        errors.append(f"'{name}' has a sortDate/endDate that isn't YYYY-MM-DD")
        continue

    # Same rule the page uses: an event is past once its last day has gone.
    last_day = event.get("endDate") or event.get("sortDate") or ""
    if last_day >= today:
        upcoming.append(event)
        if "tba" in str(event.get("date", "")).lower():
            warnings.append(f"'{name}' is upcoming but its date is still TBA")

    link = str(event.get("link") or "")
    if link and not link.startswith("https://"):
        warnings.append(f"'{name}' has a link that isn't a full https:// address")
    elif not link and last_day >= today:
        warnings.append(f"'{name}' is upcoming but has no link")

if len(upcoming) < MIN_UPCOMING:
    message = f"Only {len(upcoming)} upcoming event(s) - fewer than {MIN_UPCOMING}. Time to check SOURCES.md for more."
    if os.environ.get("GITHUB_EVENT_NAME") == "schedule":
        errors.append(message)
    else:
        warnings.append(message)

for message in warnings:
    print(f"::warning file=events.json::{message}")
for message in errors:
    print(f"::error file=events.json::{message}")
print(f"{len(events)} events, {len(upcoming)} upcoming - {len(errors)} error(s), {len(warnings)} warning(s).")
sys.exit(1 if errors else 0)
