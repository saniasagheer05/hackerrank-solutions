# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
# Problem     Diagonal Difference
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:25 p.m.
# Technique   single-pass-diagonal-summation
# Time        O(n)
# Space       O(1)
# Insight     The algorithm iterates through the matrix rows once, accumulating values from the primary diagonal at index [i][i] and the secondary diagonal at index [i][n - 1 - i] simultaneously.
# Interview   Before: "I would iterate through the matrix twice to sum each diagonal separately." After: "I can compute both sums in a single O(n) pass by using the row index to calculate both column offsets, which is optimal for an n by n matrix."
# Pitfalls    (1) Confusing the secondary diagonal index calculation n - 1 - i with n - i, which would cause an index out of bounds error.  (2) Failing to use the absolute value function abs() on the final difference, as required by the problem statement.
# ──────────────────────────────────────────────────


def diagonalDifference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        left += arr[i][i]
        right += arr[i][n - 1 - i]

    return abs(left - right)


n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

print(diagonalDifference(arr))
