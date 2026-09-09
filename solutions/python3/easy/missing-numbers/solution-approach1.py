# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
# Problem     Missing Numbers
# Difficulty  Easy
# Subdomain   Search
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 08:06 p.m.
# Technique   frequency-map-comparison
# Time        O(m + n + k log k)
# Space       O(m + n)
# Insight     The algorithm identifies missing numbers by comparing the frequency counts of each integer in the original array against the modified array, retaining only those with a higher frequency in the original.
# Interview   Before: "I would sort both arrays and use two pointers to find differences." After: "Using hash maps to compare frequencies is more efficient, achieving O(m + n) time complexity, which handles the frequency requirement and the constraint that the range of values is small."
# Pitfalls    (1) Failing to account for the requirement that missing numbers must be returned in ascending order.  (2) Assuming that checking for existence in a set is sufficient, ignoring the requirement to match exact frequency counts between the two arrays.
# ──────────────────────────────────────────────────

from collections import Counter

def missingNumbers(arr, brr):
    count_arr = Counter(arr)
    count_brr = Counter(brr)

    result = []

    for num in count_brr:
        if count_brr[num] > count_arr[num]:
            result.append(num)

    return sorted(result)


n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

answer = missingNumbers(arr, brr)

print(*answer)
