# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# Problem     Electronics Shop
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 07:22 p.m.
# ──────────────────────────────────────────────────

def getMoneySpent(keyboards, drives, b):
    max_spent = -1

    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive

            if total <= b:
                max_spent = max(max_spent, total)

    return max_spent


# Input
b, n, m = map(int, input().split())
keyboards = list(map(int, input().split()))
drives = list(map(int, input().split()))

print(getMoneySpent(keyboards, drives, b))
