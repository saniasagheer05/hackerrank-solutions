# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
# Problem     Viral Advertising
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 07:58 p.m.
# ──────────────────────────────────────────────────

def viralAdvertising(n):
    shared = 5
    total_likes = 0

    for day in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3

    return total_likes


n = int(input())
print(viralAdvertising(n))
