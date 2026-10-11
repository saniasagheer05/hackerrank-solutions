# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
# Problem     Extra Long Factorials
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 12:30 a.m.
# ──────────────────────────────────────────────────


def extraLongFactorials(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

n = int(input().strip())
extraLongFactorials(n)
