#!/usr/bin/env python3
"""Build the Twilio API tube-style map.

35 APIs grouped into 9 product lines mirroring Twilio's product nav:
Voice, Messaging & Email, Video & Media, Verify & Lookup, Numbers &
Routing, Engagement Apps, IoT, Platform, Ops & Insights. No interchange
hubs — Twilio's product domains are largely separate so the map renders
as a clean set of color-coded islands.

The shared rendering engine lives at .claude/skills/_subway_engine.py.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "SendGrid Email": "SendGrid",
}

LINES = [
    {
        "name": "Voice",
        "color": "#E0245E",  # central-line red
        "stations": [
            ("Voice",         (290, 170)),
            ("Trunking",      (450, 170)),
            ("Conversations", (610, 170)),
        ],
    },
    {
        "name": "Video & Media",
        "color": "#7B3FE4",  # purple
        # small arc tucked in the top-right
        "stations": [
            ("Video", (790, 175)),
            ("Media", (940, 205)),
        ],
    },
    {
        "name": "Messaging & Email",
        "color": "#E68B1F",  # orange
        "stations": [
            ("Messaging",      (290, 280)),
            ("SendGrid Email", (410, 280)),
            ("IP Messaging",   (550, 280)),
            ("Notify",         (680, 280)),
            ("Content",        (820, 280)),
        ],
    },
    {
        "name": "Verify & Lookup",
        "color": "#C5318B",  # magenta
        # vertical strip on the right
        "stations": [
            ("Verify",    (1020, 250)),
            ("Lookup",    (1020, 320)),
            ("Trust Hub", (1020, 390)),
        ],
    },
    {
        "name": "Numbers & Routing",
        "color": "#0E9D6E",  # forest green
        # vertical strip on the left
        "stations": [
            ("Numbers", (260, 360)),
            ("Routes",  (260, 430)),
            ("Proxy",   (260, 500)),
        ],
    },
    {
        "name": "Engagement Apps",
        "color": "#0B7956",  # deeper green
        "stations": [
            ("Studio",    (380, 450)),
            ("Autopilot", (510, 450)),
            ("Assistant", (640, 450)),
            ("Flex",      (770, 450)),
            ("Frontline", (900, 450)),
        ],
    },
    {
        "name": "IoT",
        "color": "#1E5BD0",  # royal blue
        "stations": [
            ("Super Sim",  (380, 570)),
            ("Wireless",   (560, 570)),
            ("Microvisor", (740, 570)),
        ],
    },
    {
        "name": "Platform",
        "color": "#5A6275",  # slate
        "stations": [
            ("Accounts",     (260, 680)),
            ("Pricing",      (370, 680)),
            ("Serverless",   (480, 680)),
            ("Sync",         (585, 680)),
            ("Task Router",  (700, 680)),
            ("Bulk Exports", (815, 680)),
            ("Marketplace",  (925, 680)),
        ],
    },
    {
        "name": "Ops & Insights",
        "color": "#B89719",  # mustard
        "stations": [
            ("Insights",     (380, 800)),
            ("Intelligence", (555, 800)),
            ("Monitor",      (725, 800)),
            ("Events",       (900, 800)),
        ],
    },
]


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)

    build_subway(
        title="The Twilio API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · "
                 f"click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: twilio/openapi/*-openapi.yml · github.com/api-evangelist/twilio",
        out_dir=Path(__file__).resolve().parent,
        out_basename="twilio-subway-map",
        provider_id="twilio",
    )


if __name__ == "__main__":
    main()
