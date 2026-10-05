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
# Interview   Before: "I could use mathematical modulo operations to reverse the integer." After: "Using string slicing is more concise in Python, resulting in O((j-i) * log10(j)) time complexity, where log10(j) represents the number of digits in the largest day value."
# Pitfalls    (1) The range function range(i, j + 1) is required to ensure the upper bound j is included in the calculation.  (2) Reversing an integer using string slicing handles trailing zeros correctly, as int('021') evaluates to 21.
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
