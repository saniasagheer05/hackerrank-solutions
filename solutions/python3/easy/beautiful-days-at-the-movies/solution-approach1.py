# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
# Problem     Beautiful Days at the Movies
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 07:57 p.m.
# Technique   string-reversal-iteration
# Time        O((j-i) * log10(j))
# Space       O(log10(j))
# Insight     The algorithm iterates through the inclusive range [i, j], calculating the absolute difference between each integer and its reversed string representation to verify divisibility by k.
# Interview   Before: "I would convert the number to a string, reverse it, and check the modulo." After: "I implemented a linear scan over the range [i, j] with O((j-i) * log10(j)) time complexity, ensuring the absolute difference is divisible by k as specified in the problem constraints."
# Pitfalls    (1) The range function range(i, j + 1) is required to ensure the upper bound j is included in the calculation.  (2) Reversing the integer using string slicing [::-1] correctly handles trailing zeros by converting them to leading zeros in the reversed string before casting back to an integer.
# ──────────────────────────────────────────────────

def beautifulDays(i, j, k):
    count = 0

    for day in range(i, j + 1):
        reverse_day = int(str(day)[::-1])

        if abs(day - reverse_day) % k == 0:
            count += 1

    return count


i, j, k = map(int, input().split())
print(beautifulDays(i, j, k))
