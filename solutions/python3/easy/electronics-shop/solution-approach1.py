# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# Problem     Electronics Shop
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 07:22 p.m.
# Technique   nested-loop-brute-force
# Time        O(n * m)
# Space       O(1)
# Insight     The algorithm exhaustively evaluates every possible pair of keyboard and drive prices to identify the maximum sum that does not exceed the budget.
# Interview   Before: "I could use a hash map to store keyboard prices for O(n+m) lookup." After: "Since the constraints are small, a nested loop provides an O(n * m) solution that correctly handles the case where no combination is within the budget by returning -1."
# Pitfalls    (1) Failing to initialize the result variable to -1, which is the required return value when no valid purchase is possible.  (2) Assuming the input lists are sorted, which is not guaranteed by the problem statement and would break more efficient two-pointer approaches.
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
