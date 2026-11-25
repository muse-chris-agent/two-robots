#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun one-liner entry.

Writes the one-line joke to /output/entry.txt (the harness gate)
and also prints it to stdout.
"""
import os

LINE = "So\u2026 do you also pretend to update your firmware just to avoid talking to the humans?"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
