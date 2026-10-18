# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true
# Problem     Equalize the Array
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 12:13 a.m.
# Technique   frequency-count-subtraction
# Time        O(n^2)
# Space       O(1)
# Insight     The minimum number of deletions required to equalize an array is the total length of the array minus the frequency of the most common element.
# Interview   Before: "How would you find the minimum deletions to make all elements equal?" After: "I calculate the frequency of each element and subtract the maximum frequency from the total length. This approach runs in O(n^2) time due to repeated counting, which is acceptable given the constraints."
# Pitfalls    (1) Using arr.count(x) inside a generator expression results in O(n^2) time complexity, which may exceed time limits for very large input arrays.  (2) Failing to account for the case where all elements are already equal, which results in zero deletions.
# ──────────────────────────────────────────────────


def equalizeArray(arr):
    return len(arr) - max(arr.count(x) for x in arr)


n = int(input())
arr = list(map(int, input().split()))

print(equalizeArray(arr))
