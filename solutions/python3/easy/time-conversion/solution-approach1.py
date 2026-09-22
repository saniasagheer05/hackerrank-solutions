# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# Problem     Time Conversion
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:47 p.m.
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
