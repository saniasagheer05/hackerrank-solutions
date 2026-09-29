# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
# Problem     Cats and a Mouse
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 07:24 p.m.
# ──────────────────────────────────────────────────

def catAndMouse(x, y, z):
    cat_a = abs(x - z)
    cat_b = abs(y - z)

    if cat_a < cat_b:
        return "Cat A"
    elif cat_b < cat_a:
        return "Cat B"
    else:
        return "Mouse C"


# Input
q = int(input())

for _ in range(q):
    x, y, z = map(int, input().split())
    print(catAndMouse(x, y, z))
