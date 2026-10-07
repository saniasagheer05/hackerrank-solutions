# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
# Problem     Circular Array Rotation
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 11:33 p.m.
# Technique   modular-index-mapping
# Time        O(n + q)
# Space       O(q)
# Insight     The algorithm maps each query index to its original position in the array by subtracting the effective rotation count modulo the array length.
# Interview   Before: "I would simulate the rotations by shifting elements in the array k times." After: "That would be O(n*k), which is inefficient. Instead, I use modular arithmetic to calculate the original index in O(1) per query, resulting in O(n+q) total time complexity."
# Pitfalls    (1) Failing to apply the modulo operator to k, which causes index out of bounds errors when k is greater than the array length.  (2) Incorrectly calculating the original index as (i + k) % n instead of (i - k) % n, which reverses the rotation direction.
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
