# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# Problem     Birthday Cake Candles
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:35 p.m.
# Technique   max-value-frequency-count
# Time        O(n)
# Space       O(n)
# Insight     The algorithm identifies the maximum height in the list and counts its occurrences using the built-in count method.
# Interview   Before: "I would sort the array and count the tail elements." After: "Sorting is O(n log n), but using max() and count() achieves O(n) time complexity, which is optimal for processing the candle heights list."
# Pitfalls    (1) Assuming the input list is empty, though the constraints imply n >= 1.  (2) Overlooking that max() and count() each perform a full pass over the list, resulting in two linear scans.
# ──────────────────────────────────────────────────

n = int(input())
candles = list(map(int, input().split()))

print(candles.count(max(candles)))
