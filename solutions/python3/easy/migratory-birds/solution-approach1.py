# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
# Problem     Migratory Birds
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:05 p.m.
# ──────────────────────────────────────────────────

n = int(input())
arr = list(map(int, input().split()))

def migratoryBirds(arr):
    counts = {}

    for bird in arr:
        counts[bird] = counts.get(bird, 0) + 1

    max_count = max(counts.values())

    for bird in sorted(counts):
        if counts[bird] == max_count:
            return bird

print(migratoryBirds(arr))
