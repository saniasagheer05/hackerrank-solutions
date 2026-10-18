# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true
# Problem     Jumping on the Clouds
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 12:11 a.m.
# Technique   greedy-lookahead-traversal
# Time        O(n)
# Space       O(1)
# Insight     The algorithm greedily prioritizes a two-step jump whenever the target cloud is safe, ensuring the minimum number of jumps by maximizing distance covered per step.
# Interview   Before: "I could use dynamic programming to find the shortest path." After: "Since we always want to jump as far as possible to minimize steps, a greedy approach is optimal. It runs in O(n) time and O(1) space, checking the index i+2 first to ensure we reach the end in the fewest jumps."
# Pitfalls    (1) Failing to check the bounds of i+2 before accessing the array, which causes an IndexError.  (2) Incorrectly prioritizing a single-step jump when a two-step jump is available, leading to a non-minimal jump count.  (3) Terminating the loop prematurely by using an incorrect condition, such as i < len(c) instead of i < len(c) - 1.
# ──────────────────────────────────────────────────


def jumpingOnClouds(c):
    jumps = 0
    i = 0

    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1

    return jumps


n = int(input())
c = list(map(int, input().split()))

print(jumpingOnClouds(c))
