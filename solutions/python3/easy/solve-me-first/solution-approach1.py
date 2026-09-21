# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/solve-me-first/problem?isFullScreen=true
# Problem     Solve Me First
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-21, 11:08 p.m.
# Technique   basic-arithmetic-sum
# Time        O(1)
# Space       O(1)
# Insight     The solution computes the sum of two provided integers using the standard addition operator.
# Interview   Before: "How would you implement a function to add two integers?" After: "The implementation uses the addition operator to return the sum in O(1) time and O(1) space, handling the input integers directly as specified."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing the addition operation.  (2) Assuming the input format might contain multiple values on a single line instead of separate lines as implied by the input calls.
# ──────────────────────────────────────────────────

a = int(input())
b = int(input())

print(a + b)
