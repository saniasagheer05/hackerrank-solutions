# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
# Problem     Simple Array Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-26, 12:04 a.m.
# ──────────────────────────────────────────────────

def simpleArraySum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))

print(simpleArraySum(ar))
