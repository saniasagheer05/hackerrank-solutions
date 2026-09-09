# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# Problem     Ice Cream Parlor
# Difficulty  Easy
# Subdomain   Search
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 08:08 p.m.
# Technique   hash-map-complement-lookup
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the cost array once, storing each price in a hash map to enable O(1) lookup of the required complement that sums to the target money.
# Interview   Before: "I could use a nested loop to check every pair, but that would be O(n^2)." After: "By using a hash map to store previously seen prices, I can find the complement in O(n) time, ensuring I meet the 1-based indexing requirement efficiently."
# Pitfalls    (1) Failing to convert 0-based loop indices to 1-based indices as required by the problem statement.  (2) Assuming the input array might contain multiple pairs when the problem guarantees a unique solution.  (3) Overwriting existing keys in the hash map if duplicate prices exist, though the problem's unique solution constraint mitigates this risk.
# ──────────────────────────────────────────────────

def icecreamParlor(m, cost):
    seen = {}

    for i, price in enumerate(cost):
        needed = m - price

        if needed in seen:
            return [seen[needed] + 1, i + 1]

        seen[price] = i


t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))

    result = icecreamParlor(m, cost)
    print(result[0], result[1])
