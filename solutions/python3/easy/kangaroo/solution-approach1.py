# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# Problem     Number Line Jumps
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-23, 08:24 p.m.
# ──────────────────────────────────────────────────

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    numerator = x2 - x1
    denominator = v1 - v2

    if numerator % denominator == 0 and numerator // denominator >= 0:
        return "YES"
    
    return "NO"


x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))
