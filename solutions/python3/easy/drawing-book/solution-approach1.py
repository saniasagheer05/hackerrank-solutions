# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# Problem     Drawing Book 
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:00 p.m.
# Technique   integer-division-math
# Time        O(1)
# Space       O(1)
# Insight     The number of page turns from the front is determined by integer division of the target page by two, while the turns from the back are calculated by subtracting that value from the total page pairs.
# Interview   Before: "I should simulate the page flips with a loop." After: "Since each turn reveals two pages, we can calculate the distance from both ends in O(1) time using integer division, which handles the last page parity correctly."
# Pitfalls    (1) Assuming the last page always has two sides, which ignores the problem statement that the last page may only be printed on the front.  (2) Failing to account for the fact that page 1 is always on the right, making the first turn count as zero.
# ──────────────────────────────────────────────────

def pageCount(n, p):
    from_front = p // 2
    from_back = n // 2 - p // 2
    
    return min(from_front, from_back)


n = int(input())
p = int(input())

print(pageCount(n, p))
