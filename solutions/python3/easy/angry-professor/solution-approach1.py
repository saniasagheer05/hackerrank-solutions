# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
# Problem     Angry Professor
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-03, 11:32 p.m.
# ──────────────────────────────────────────────────

def angryProfessor(k, a):
    count = 0

    for x in a:
        if x <= 0:
            count += 1

    if count < k:
        return "YES"
    else:
        return "NO"


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(angryProfessor(k, a))
