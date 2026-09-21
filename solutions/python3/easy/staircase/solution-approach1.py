# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
# Problem     Staircase
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-21, 11:06 p.m.
# Technique   string-multiplication-loop
# Time        O(n^2)
# Space       O(n)
# Insight     The algorithm iterates from one to n, printing a line where the number of leading spaces is n minus the current index and the number of hash symbols is the current index.
# Interview   Before: I could use nested loops to print each character individually. After: Using Python's string multiplication is more idiomatic and efficient, resulting in O(n^2) time complexity because each of the n lines contains up to n characters.
# Pitfalls    (1) Using range(n) instead of range(1, n + 1) results in an empty first line and a missing final line of size n.  (2) Swapping the order of space and hash multiplication creates a left-aligned staircase instead of the required right-aligned format.
# ──────────────────────────────────────────────────

def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

n = int(input())
staircase(n)
