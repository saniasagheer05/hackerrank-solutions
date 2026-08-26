# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
# Problem     Mini-Max Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-27, 12:37 a.m.
# ──────────────────────────────────────────────────

arr = list(map(int, input().split()))

total = sum(arr)

minimum = total - max(arr)
maximum = total - min(arr)

print(minimum, maximum)
