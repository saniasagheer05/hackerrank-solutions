# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
# Problem     Compare the Triplets
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-26, 12:10 a.m.
# Technique   linear-scan-comparison
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through the fixed-length triplets, incrementing the respective score counter only when a strict inequality between corresponding elements is satisfied.
# Interview   Before: "I could use a dictionary to map indices to scores." After: "Since the input size is fixed at three, a simple linear scan with O(1) time and O(1) space is optimal for comparing the triplets."
# Pitfalls    (1) Failing to handle the equality case where neither Alice nor Bob receives a point.  (2) Incorrectly returning the scores in the wrong order, as the problem requires Alice's score first.
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
