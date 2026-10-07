# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# Problem     Sequence Equation
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 11:34 p.m.
# Technique   inverse-mapping-array
# Time        O(n)
# Space       O(n)
# Insight     The algorithm constructs an inverse mapping array where each index stores the position of the value, allowing the composition p(p(y)) = x to be solved by two lookups in O(1) time.
# Interview   Before: "How would you find y such that p(p(y)) = x for all x?" After: "I precompute the inverse mapping of the permutation in O(n) time, then perform two lookups for each x to achieve O(n) total time and O(n) space complexity."
# Pitfalls    (1) Confusing 1-based indexing of the problem with 0-based indexing of the input array.  (2) Failing to allocate the inverse mapping array with size n+1 to accommodate values up to n.
# ──────────────────────────────────────────────────

def permutationEquation(p):
    n = len(p)
    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i + 1

    result = []

    for x in range(1, n + 1):
        result.append(pos[pos[x]])

    return result


n = int(input())
p = list(map(int, input().split()))

answer = permutationEquation(p)

for x in answer:
    print(x)
