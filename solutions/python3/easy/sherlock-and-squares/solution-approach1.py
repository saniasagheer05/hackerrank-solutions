# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
# Problem     Sherlock and Squares
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:22 p.m.
# Technique   integer-square-root-difference
# Time        O(1)
# Space       O(1)
# Insight     The number of perfect squares in an inclusive range [a, b] is calculated by finding the difference between the integer square roots of the upper bound and the value immediately preceding the lower bound.
# Interview   Before: "I should iterate from a to b and check if each number is a perfect square." After: "Iterating is inefficient for large ranges. Instead, I use math.isqrt to find the count in O(1) time by subtracting the square root of a-1 from the square root of b."
# Pitfalls    (1) Failing to use a-1 as the lower bound, which incorrectly excludes the lower boundary if it is a perfect square.  (2) Assuming floating-point math.sqrt is sufficient, which risks precision errors for very large integers compared to math.isqrt.
# ──────────────────────────────────────────────────


import math

def squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        a, b = map(int, input().split())
        print(squares(a, b))
