# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
# Problem     Cats and a Mouse
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 07:24 p.m.
# Technique   absolute-difference-comparison
# Time        O(1)
# Space       O(1)
# Insight     The algorithm determines the winner by comparing the absolute distances of each cat from the mouse's position, returning the cat with the smaller distance or a tie if distances are equal.
# Interview   Before: "I should calculate the distance for each cat and compare them." After: "By calculating the absolute difference for each cat in O(1) time, I can determine the winner or identify a tie when distances are equal, handling all input cases efficiently."
# Pitfalls    (1) Confusing the return strings 'Cat A', 'Cat B', or 'Mouse C' with incorrect casing or spacing.  (2) Failing to use the absolute value function, which would lead to incorrect results when a cat's position is less than the mouse's position.
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
