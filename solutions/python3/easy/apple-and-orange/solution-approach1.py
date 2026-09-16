# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# Problem     Apple and Orange
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:16 a.m.
# Technique   linear-scan-range-check
# Time        O(m + n)
# Space       O(1)
# Insight     The algorithm calculates the absolute landing position of each fruit by adding its displacement to the tree's coordinate and verifies if the result falls within the inclusive range defined by the house boundaries.
# Interview   Before: "I should probably sort the fruit positions to use binary search." After: "Since we must check every fruit, a linear scan is optimal with O(m + n) time complexity, where m and n are the counts of apples and oranges respectively."
# Pitfalls    (1) Confusing the inclusive range [s, t] with an exclusive range, which would lead to incorrect counts for fruits landing exactly on s or t.  (2) Neglecting to add the tree's coordinate (a or b) to the displacement distance, resulting in checking the displacement value instead of the absolute position.
# ──────────────────────────────────────────────────

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for distance in apples:
        position = a + distance
        if s <= position <= t:
            apple_count += 1

    for distance in oranges:
        position = b + distance
        if s <= position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
