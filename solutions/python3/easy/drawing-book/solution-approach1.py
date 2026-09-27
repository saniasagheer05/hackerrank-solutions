# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# Problem     Drawing Book 
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:00 p.m.
# ──────────────────────────────────────────────────

def pageCount(n, p):
    from_front = p // 2
    from_back = n // 2 - p // 2
    
    return min(from_front, from_back)


n = int(input())
p = int(input())

print(pageCount(n, p))
