# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
# Problem     Migratory Birds
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 03:05 p.m.
# Technique   hash-map-frequency-counting
# Time        O(N log K)
# Space       O(K)
# Insight     The algorithm counts occurrences of each bird type in a hash map and iterates through sorted keys to identify the smallest ID associated with the maximum frequency.
# Interview   Before: "I could use a frequency array since bird IDs are small." After: "Using a hash map and sorting keys provides an O(N log K) solution, where K is the number of unique bird types, ensuring we return the smallest ID when frequencies tie."
# Pitfalls    (1) Failing to sort the keys before iterating prevents returning the smallest ID in the event of a frequency tie.  (2) Assuming bird IDs are contiguous or start at one, though the hash map approach correctly handles any integer IDs.
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
