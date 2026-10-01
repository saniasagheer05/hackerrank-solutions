# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
# Problem     The Hurdle Race
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-01, 09:21 p.m.
# Technique   maximum-value-difference
# Time        O(n)
# Space       O(n)
# Insight     The character requires a number of doses equal to the difference between the maximum hurdle height and the initial jump capacity, or zero if the capacity is already sufficient.
# Interview   Before: "I would iterate through the list to find the tallest hurdle and subtract the jump capacity." After: "The solution uses max() to find the tallest hurdle in O(n) time, then returns the difference or zero, ensuring the result is non-negative as required by the problem constraints."
# Pitfalls    (1) Failing to handle the case where the maximum hurdle height is less than or equal to the initial jump capacity k.  (2) Assuming the input list height is empty, though the constraints imply n >= 1.
# ──────────────────────────────────────────────────

def hurdleRace(k, height):
    tallest = max(height)
    return max(0, tallest - k)

n, k = map(int, input().split())
height = list(map(int, input().split()))


print(hurdleRace(k, height))
