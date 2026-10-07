# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# Problem     Sequence Equation
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 11:34 p.m.
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
