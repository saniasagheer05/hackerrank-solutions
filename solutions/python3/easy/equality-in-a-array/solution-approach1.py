# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true
# Problem     Equalize the Array
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 12:13 a.m.
# ──────────────────────────────────────────────────


def equalizeArray(arr):
    return len(arr) - max(arr.count(x) for x in arr)


n = int(input())
arr = list(map(int, input().split()))

print(equalizeArray(arr))
