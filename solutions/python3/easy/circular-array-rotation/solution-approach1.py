# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
# Problem     Circular Array Rotation
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 11:33 p.m.
# ──────────────────────────────────────────────────

def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n

    result = []

    for i in queries:
        result.append(a[(i - k) % n])

    return result


n, k, q = map(int, input().split())
a = list(map(int, input().split()))

queries = []
for _ in range(q):
    queries.append(int(input()))

answer = circularArrayRotation(a, k, queries)

for x in answer:
    print(x)
