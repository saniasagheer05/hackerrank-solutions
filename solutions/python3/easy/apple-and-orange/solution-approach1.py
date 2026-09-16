# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# Problem     Apple and Orange
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:16 a.m.
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
