#!/usr/bin/env python3
"""Build the Twilio API tube-style map.

35 APIs grouped into 9 product lines mirroring Twilio's product nav.
Lines use varied shapes — arcs, L-bends, sine waves, and small islands —
so the map reads as a real underground network rather than parallel rules.

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
        "color": "#E0245E",
        # Convex-down arc: dips in the middle then rises again.
        "stations": [
            ("Voice",         (290, 200)),
            ("Trunking",      (450, 150)),
            ("Conversations", (620, 200)),
        ],
    },
    {
        "name": "Video & Media",
        "color": "#7B3FE4",
        # Diagonal sweep up-right.
        "stations": [
            ("Video", (760, 190)),
            ("Media", (940, 155)),
        ],
    },
    {
        "name": "Messaging & Email",
        "color": "#E68B1F",
        # Sine wave across the top-middle band.
        "stations": [
            ("Messaging",      (270, 295)),
            ("SendGrid Email", (400, 265)),
            ("IP Messaging",   (540, 300)),
            ("Notify",         (680, 265)),
            ("Content",        (820, 295)),
        ],
    },
    {
        "name": "Verify & Lookup",
        "color": "#C5318B",
        # Vertical with a subtle inward bow.
        "stations": [
            ("Verify",    (1000, 250)),
            ("Lookup",    (1025, 320)),
            ("Trust Hub", (1000, 390)),
        ],
    },
    {
        "name": "Numbers & Routing",
        "color": "#0E9D6E",
        # L-shape: vertical drop, then bends 45° to the right at the bottom.
        "stations": [
            ("Numbers", (260, 370)),
            ("Routes",  (260, 440)),
            ("Proxy",   (320, 510)),
        ],
    },
    {
        "name": "Engagement Apps",
        "color": "#0B7956",
        # Concave-up arc — middle stations sit higher than the endpoints.
        "stations": [
            ("Studio",    (370, 480)),
            ("Autopilot", (495, 445)),
            ("Assistant", (625, 430)),
            ("Flex",      (760, 445)),
            ("Frontline", (905, 480)),
        ],
    },
    {
        "name": "IoT",
        "color": "#1E5BD0",
        # Short curve dipping up in the middle.
        "stations": [
            ("Super Sim",  (380, 590)),
            ("Wireless",   (560, 555)),
            ("Microvisor", (740, 590)),
        ],
    },
    {
        "name": "Platform",
        "color": "#5A6275",
        # Sine wave — alternating up and down.
        "stations": [
            ("Accounts",     (260, 705)),
            ("Pricing",      (365, 670)),
            ("Serverless",   (475, 705)),
            ("Sync",         (585, 670)),
            ("Task Router",  (695, 705)),
            ("Bulk Exports", (810, 670)),
            ("Marketplace",  (925, 705)),
        ],
    },
    {
        "name": "Ops & Insights",
        "color": "#B89719",
        # Inverse wave (offset half-phase from Platform above) for visual rhythm.
        "stations": [
            ("Insights",     (380, 790)),
            ("Intelligence", (555, 815)),
            ("Monitor",      (730, 790)),
            ("Events",       (905, 815)),
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
