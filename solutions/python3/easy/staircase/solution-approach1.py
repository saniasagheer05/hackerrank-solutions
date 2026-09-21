# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
# Problem     Staircase
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-21, 11:06 p.m.
# ──────────────────────────────────────────────────

def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

n = int(input())
staircase(n)
