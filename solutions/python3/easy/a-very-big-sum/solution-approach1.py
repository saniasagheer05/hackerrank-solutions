# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true
# Problem     A Very Big Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-27, 12:30 a.m.
# Technique   built-in-sum-function
# Time        O(n)
# Space       O(n)
# Insight     The implementation utilizes Python's native sum function to aggregate all elements in the list, which automatically handles arbitrary-precision integers.
# Interview   Before: "How would you handle potential integer overflow when summing these large values?" After: "Python handles large integers automatically, so the built-in sum function is sufficient. This approach runs in O(n) time and O(n) space, effectively managing the 10^10 constraint per element."
# Pitfalls    (1) Assuming 32-bit integer overflow limits apply to Python, which natively supports arbitrary-precision integers.  (2) Failing to account for the O(n) space complexity required to store the input array in memory.
# ──────────────────────────────────────────────────

n = int(input())
ar = list(map(int, input().split()))

print(sum(ar))
