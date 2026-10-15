# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
# Problem     Library Fine
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:23 p.m.
# Technique   hierarchical-conditional-date-comparison
# Time        O(1)
# Space       O(1)
# Insight     The algorithm evaluates lateness by checking the most significant time unit first, ensuring that only the least precise measure of lateness determines the fine.
# Interview   Before: "I would calculate the total days difference between the two dates." After: "That approach is unnecessary because the problem defines specific, non-overlapping fine tiers. I used a hierarchical conditional structure to check year, then month, then day, resulting in O(1) time complexity and handling the fixed year-late fine correctly."
# Pitfalls    (1) Failing to prioritize the year check, which incorrectly calculates a fine for early returns in later years.  (2) Incorrectly applying the 15-Hacko multiplier to months or years instead of just days.  (3) Returning a non-zero fine when the return date is before the due date, violating the rule that no fine is charged for on-time returns.
# ──────────────────────────────────────────────────


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0
    elif m1 > m2:
        return 500 * (m1 - m2)
    elif m1 < m2:
        return 0
    elif d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0


if __name__ == '__main__':
    d1, m1, y1 = map(int, input().split())
    d2, m2, y2 = map(int, input().split())

    print(libraryFine(d1, m1, y1, d2, m2, y2))
