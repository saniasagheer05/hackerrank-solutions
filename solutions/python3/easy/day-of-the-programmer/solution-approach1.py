# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# Problem     Day of the Programmer
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:02 p.m.
# Technique   conditional-calendar-logic
# Time        O(1)
# Space       O(1)
# Insight     The implementation branches logic based on the specific calendar system in effect for the given year, handling the Julian, Gregorian, and the unique 1918 transition year separately.
# Interview   Before: "I would calculate the day by summing months." After: "The problem requires O(1) logic to handle three distinct calendar rules: Julian leap years, Gregorian leap years, and the 1918 transition where February 14th followed January 31st."
# Pitfalls    (1) Failing to account for the 1918 transition year where the 256th day is shifted due to the calendar change.  (2) Applying Gregorian leap year rules to years before 1918 instead of the Julian rule of divisibility by 4.  (3) Incorrectly calculating the day offset for non-leap years versus leap years in the Gregorian calendar.
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
