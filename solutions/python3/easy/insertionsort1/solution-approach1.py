# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
# Problem     Insertion Sort - Part 1
# Difficulty  Easy
# Subdomain   Sorting
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 08:08 p.m.
# ──────────────────────────────────────────────────

n = int(input())
arr = list(map(int, input().split()))

x = arr[-1]
i = n - 2

while i >= 0:
    if arr[i] > x:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    else:
        break

arr[i + 1] = x
print(*arr)
