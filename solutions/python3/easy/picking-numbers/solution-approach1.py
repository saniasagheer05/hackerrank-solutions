# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
# Problem     Picking Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 07:45 p.m.
# Technique   frequency-count-scan
# Time        O(n^2)
# Space       O(1)
# Insight     The algorithm calculates the maximum subarray length by iterating through each unique element and summing its occurrences with the occurrences of its successor.
# Interview   Before: "I would use a sliding window to find the longest subarray." After: "Since the problem allows any elements with a difference of at most one, I can simply count occurrences of x and x+1 for each element, resulting in O(n^2) time complexity."
# Pitfalls    (1) The O(n^2) time complexity may exceed execution limits for large input sizes where n is up to 100.  (2) The implementation performs redundant counting by re-scanning the entire array for every element in the input list.
# ──────────────────────────────────────────────────

def pickingNumbers(a):
    max_length = 0

    for x in a:
        count = a.count(x) + a.count(x + 1)
        max_length = max(max_length, count)

    return max_length


n = int(input())
a = list(map(int, input().split()))

print(pickingNumbers(a))
