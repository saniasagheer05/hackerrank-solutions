# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# Problem     Birthday Cake Candles
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:35 p.m.
# ──────────────────────────────────────────────────

n = int(input())
candles = list(map(int, input().split()))

print(candles.count(max(candles)))
