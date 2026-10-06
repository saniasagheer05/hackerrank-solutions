# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
# Problem     Save the Prisoner!
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 09:34 p.m.
# Technique   modular-arithmetic-offset
# Time        O(1)
# Space       O(1)
# Insight     The formula calculates the final chair position by shifting the starting chair to zero-indexed, adding the number of sweets, taking the modulo of the total prisoners, and converting back to one-indexed.
# Interview   Before: "I would simulate the distribution by iterating through the prisoners one by one." After: "That would be O(m) time, which is too slow for large inputs. Using modular arithmetic, we can solve this in O(1) time by calculating the final position directly, handling the circular wrap-around correctly."
# Pitfalls    (1) Failing to convert the one-based indexing to zero-based before applying the modulo operator.  (2) Neglecting to add one back to the result after the modulo operation to restore one-based indexing.  (3) Miscalculating the offset by using s + m - 1 instead of s + m - 2 when adjusting for the starting position.
# ──────────────────────────────────────────────────

def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1


t = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())
    print(saveThePrisoner(n, m, s))
    
