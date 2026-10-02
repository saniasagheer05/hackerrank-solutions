# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
# Problem     Utopian Tree
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:34 p.m.
# Technique   iterative-cycle-simulation
# Time        O(n)
# Space       O(1)
# Insight     The tree height updates by doubling during even-indexed cycles and incrementing by one during odd-indexed cycles, starting from an initial height of one.
# Interview   Before: "I could use a mathematical formula to calculate the height based on the parity of n." After: "Since the constraints on n are small, an O(n) iterative simulation is efficient and directly maps to the growth rules for each cycle."
# Pitfalls    (1) Misinterpreting the cycle index, as the loop uses zero-based indexing where even indices represent spring growth and odd indices represent summer growth.  (2) Assuming the initial height of one is modified before the first cycle, whereas the loop correctly processes n cycles starting from the initial height.
# ──────────────────────────────────────────────────

def utopianTree(n):
    height = 1

    for i in range(n):
        if i % 2 == 0:
            height = height * 2
        else:
            height = height + 1

    return height


t = int(input())

for _ in range(t):
    n = int(input())
    print(utopianTree(n))
