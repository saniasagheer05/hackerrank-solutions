# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
# Problem     Divisible Sum Pairs
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-24, 07:02 p.m.
# Technique   nested-loop-brute-force
# Time        O(n^2)
# Space       O(1)
# Insight     The algorithm iterates through all unique pairs (i, j) where i < j and increments a counter whenever the sum of the elements at those indices is divisible by k.
# Interview   Before: "I could use a hash map to track remainders for O(n) time." After: "Given the constraints, a nested loop approach is sufficient with O(n^2) time complexity, ensuring we only check pairs where i < j as required by the problem statement."
# Pitfalls    (1) Failing to enforce the i < j constraint leads to double-counting pairs or including self-pairs.  (2) Assuming the input array is sorted, which is not guaranteed by the problem statement.  (3) Neglecting the modulo operator behavior with negative numbers if the input array contained negative integers.
# ──────────────────────────────────────────────────

n, k = map(int, input().split())
ar = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if (ar[i] + ar[j]) % k == 0:
            count += 1

print(count)
