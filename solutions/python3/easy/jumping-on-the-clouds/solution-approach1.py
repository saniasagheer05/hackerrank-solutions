# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true
# Problem     Jumping on the Clouds
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 12:11 a.m.
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
