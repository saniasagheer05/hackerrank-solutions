# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
# Problem     Extra Long Factorials
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 12:30 a.m.
# Technique   iterative-multiplication-arbitrary-precision
# Time        O(n^2)
# Space       O(n log n)
# Insight     The implementation leverages Python's native arbitrary-precision integer support to compute the product of all integers from one to n iteratively.
# Interview   Before: "How would you handle factorials exceeding 64-bit limits?" After: "Python handles large integers automatically, so we use an iterative loop to multiply values. The time complexity is O(n^2) due to the cost of multiplying increasingly large numbers, which is necessary for n up to 100."
# Pitfalls    (1) Assuming standard 64-bit integer overflow behavior in languages like C++ when Python handles arbitrary-precision integers natively.  (2) Failing to account for the O(n^2) complexity of multiplying large numbers, which becomes significant as n approaches 100.
# ──────────────────────────────────────────────────


def extraLongFactorials(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

n = int(input().strip())
extraLongFactorials(n)
