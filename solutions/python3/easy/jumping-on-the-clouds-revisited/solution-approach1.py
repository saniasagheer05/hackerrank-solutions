# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
# Problem     Jumping on the Clouds: Revisited
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 11:56 p.m.
# ──────────────────────────────────────────────────


def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = 0

    while True:
        i = (i + k) % n
        energy -= 1

        if c[i] == 1:
            energy -= 2

        if i == 0:
            break

    return energy


n, k = map(int, input().split())
c = list(map(int, input().split()))

print(jumpingOnClouds(c, k))
