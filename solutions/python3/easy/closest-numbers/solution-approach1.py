# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
# Problem     Closest Numbers
# Difficulty  Easy
# Subdomain   Sorting
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 10:53 p.m.
# ──────────────────────────────────────────────────

import sys

def closestNumbers(arr):
    arr.sort()

    min_diff = arr[1] - arr[0]
    result = []

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]
        elif diff == min_diff:
            result.append(arr[i])
            result.append(arr[i + 1])

    return result


n = int(input())
arr = list(map(int, input().split()))

answer = closestNumbers(arr)

print(*answer)
