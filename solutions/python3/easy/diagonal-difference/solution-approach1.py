# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
# Problem     Diagonal Difference
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:25 p.m.
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
