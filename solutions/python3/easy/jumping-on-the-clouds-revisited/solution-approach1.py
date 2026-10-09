# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
# Problem     Jumping on the Clouds: Revisited
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 11:56 p.m.
# Technique   circular-modulo-simulation
# Time        O(n/gcd(n, k))
# Space       O(1)
# Insight     The simulation tracks energy depletion by traversing the circular array using modulo arithmetic until the index returns to the starting position.
# Interview   Before: "How would you handle the circular path and energy penalties?" After: "I use a while loop with modulo arithmetic to simulate the jumps, reducing energy by 1 per jump and 2 extra for thunderheads. This runs in O(n/gcd(n, k)) time, ensuring we stop exactly when returning to index 0."
# Pitfalls    (1) Failing to account for the additional 2-unit energy penalty when landing on a thunderhead.  (2) Incorrectly terminating the loop before the first jump completes, as the character must return to index 0.  (3) Miscalculating the circular index by omitting the modulo operator, which is required to wrap around the array.
# ──────────────────────────────────────────────────


def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = 0

    while True:
        i = (i + k) % n
        energy -= 1

        if c[i] == 1:
            energy -= 2

        if i == 0:
            break

    return energy


n, k = map(int, input().split())
c = list(map(int, input().split()))

print(jumpingOnClouds(c, k))
