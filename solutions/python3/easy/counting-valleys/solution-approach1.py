# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# Problem     Counting Valleys
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-28, 02:15 p.m.
# Technique   altitude-tracking-counter
# Time        O(n)
# Space       O(1)
# Insight     The algorithm increments the valley count only when the hiker returns to sea level from a negative altitude, signifying the completion of a valley traversal.
# Interview   Before: "I would track the current altitude and increment a counter whenever the path goes below sea level." After: "I track the altitude and increment the valley count specifically when the hiker reaches sea level from below, ensuring an O(n) time and O(1) space complexity for any number of steps."
# Pitfalls    (1) Incrementing the valley count when reaching sea level from above, which incorrectly counts mountains as valleys.  (2) Failing to account for the definition that a valley must start with a step down from sea level.  (3) Misinterpreting the sea level condition by checking for level == 0 before updating the altitude for the current step.
# ──────────────────────────────────────────────────

def countingValleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:  # step == 'D'
            level -= 1

    return valleys


steps = int(input())
path = input().strip()

print(countingValleys(steps, path))
