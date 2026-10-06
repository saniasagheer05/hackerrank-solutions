# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
# Problem     Save the Prisoner!
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 09:34 p.m.
# ──────────────────────────────────────────────────

def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1


t = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())
    print(saveThePrisoner(n, m, s))
    
