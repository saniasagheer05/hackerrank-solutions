# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# Problem     Counting Valleys
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-28, 02:15 p.m.
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
