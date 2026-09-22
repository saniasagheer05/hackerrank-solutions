# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# Problem     Time Conversion
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:47 p.m.
# Technique   string-slicing-and-conditional-logic
# Time        O(1)
# Space       O(1)
# Insight     The algorithm isolates the period and hour components to apply modular arithmetic adjustments, mapping 12-hour cycles to 24-hour military time format.
# Pitfalls    (1) Failing to handle the 12:00:00AM case, which must map to 00:00:00 instead of 12:00:00.  (2) Incorrectly adding 12 to the hour for 12:00:00PM, which should remain 12:00:00.  (3) Forgetting to format the resulting hour with a leading zero using :02d to maintain the required string length.
# ──────────────────────────────────────────────────

def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{rest}"


s = input()
print(timeConversion(s))
