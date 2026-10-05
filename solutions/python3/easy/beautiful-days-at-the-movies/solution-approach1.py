# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
# Problem     Beautiful Days at the Movies
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 07:57 p.m.
# ──────────────────────────────────────────────────

def beautifulDays(i, j, k):
    count = 0

    for day in range(i, j + 1):
        reverse_day = int(str(day)[::-1])

        if abs(day - reverse_day) % k == 0:
            count += 1

    return count


i, j, k = map(int, input().split())
print(beautifulDays(i, j, k))
