# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
# Problem     Divisible Sum Pairs
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-24, 07:02 p.m.
# ──────────────────────────────────────────────────

n, k = map(int, input().split())
ar = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if (ar[i] + ar[j]) % k == 0:
            count += 1

print(count)
