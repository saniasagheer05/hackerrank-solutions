# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
# Problem     Sherlock and Squares
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:22 p.m.
# ──────────────────────────────────────────────────


import math

def squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        a, b = map(int, input().split())
        print(squares(a, b))
