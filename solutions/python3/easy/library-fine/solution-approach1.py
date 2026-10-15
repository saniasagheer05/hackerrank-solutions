# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
# Problem     Library Fine
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:23 p.m.
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
