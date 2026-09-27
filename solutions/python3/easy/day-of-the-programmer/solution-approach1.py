# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# Problem     Day of the Programmer
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:02 p.m.
# ──────────────────────────────────────────────────

def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"

    if year < 1918:
        if year % 4 == 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)


year = int(input())
print(dayOfProgrammer(year))
