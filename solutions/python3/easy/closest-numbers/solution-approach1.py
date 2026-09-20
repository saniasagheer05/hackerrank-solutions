# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
# Problem     Closest Numbers
# Difficulty  Easy
# Subdomain   Sorting
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 10:53 p.m.
# Technique   sorting-and-linear-scan
# Time        O(n log n)
# Space       O(n)
# Insight     Sorting the array ensures that the minimum absolute difference must exist between adjacent elements, allowing a single linear pass to identify all pairs with that minimum difference.
# Interview   Before: "I could compare every pair in O(n^2) time." After: "By sorting first, I reduce the search to O(n log n) time and O(n) space, as the smallest difference is guaranteed to be between adjacent elements in the sorted list."
# Pitfalls    (1) Failing to handle multiple pairs with the same minimum difference by only storing the last found pair instead of appending to a list.  (2) Assuming the input array is already sorted, which would lead to incorrect results for unsorted inputs.  (3) Neglecting to initialize the minimum difference with the first adjacent pair, which could cause errors if the initial value is set to an arbitrary large constant.
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
