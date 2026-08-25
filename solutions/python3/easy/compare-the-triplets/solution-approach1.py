# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
# Problem     Compare the Triplets
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-26, 12:10 a.m.
# ──────────────────────────────────────────────────

a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(3):
    if a[i] > b[i]:
        alice += 1
    elif a[i] < b[i]:
        bob += 1

print(alice, bob)
