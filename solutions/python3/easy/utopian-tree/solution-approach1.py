# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
# Problem     Utopian Tree
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:34 p.m.
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
