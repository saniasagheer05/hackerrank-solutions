# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# Problem     Subarray Division
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-23, 08:25 p.m.
# ──────────────────────────────────────────────────

def birthday(s, d, m):
    count = 0

    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1

    return count


n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())

print(birthday(s, d, m))
