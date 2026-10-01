# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
# Problem     The Hurdle Race
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-01, 09:21 p.m.
# ──────────────────────────────────────────────────

def hurdleRace(k, height):
    tallest = max(height)
    return max(0, tallest - k)

n, k = map(int, input().split())
height = list(map(int, input().split()))


print(hurdleRace(k, height))
