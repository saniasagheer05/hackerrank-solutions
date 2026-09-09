# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# Problem     Ice Cream Parlor
# Difficulty  Easy
# Subdomain   Search
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 08:08 p.m.
# ──────────────────────────────────────────────────

def icecreamParlor(m, cost):
    seen = {}

    for i, price in enumerate(cost):
        needed = m - price

        if needed in seen:
            return [seen[needed] + 1, i + 1]

        seen[price] = i


t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))

    result = icecreamParlor(m, cost)
    print(result[0], result[1])
