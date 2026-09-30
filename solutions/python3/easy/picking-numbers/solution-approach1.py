# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
# Problem     Picking Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 07:44 p.m.
# ──────────────────────────────────────────────────

def pickingNumbers(a):
    max_length = 0

    for x in a:
        count = a.count(x) + a.count(x + 1)
        max_length = max(max_length, count)

    return max_length


n = int(input())
a = list(map(int, input().split()))

print(pickingNumbers(a))
