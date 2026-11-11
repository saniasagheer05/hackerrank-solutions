# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
# Problem     Minimum Distances
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 01:27 a.m.
# Technique   hash-map-last-seen-index
# Time        O(n)
# Space       O(n)
# Insight     The algorithm maintains a hash map of the most recent index for each element encountered, updating the minimum distance whenever a duplicate is found.
# Interview   Before: "I could use nested loops to compare every pair, but that is O(n^2)." After: "I can use a hash map to store the last seen index of each element, allowing me to find the minimum distance in O(n) time and O(n) space, returning -1 if no duplicates exist."
# Pitfalls    (1) Failing to handle the case where no duplicates exist, which requires returning -1 instead of infinity.  (2) Updating the last_seen index before calculating the distance, which would incorrectly result in a distance of zero.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

def minimumDistances(a):
    last_seen = {}
    min_distance = float('inf')

    for i in range(len(a)):
        if a[i] in last_seen:
            distance = i - last_seen[a[i]]
            min_distance = min(min_distance, distance)

        last_seen[a[i]] = i

    if min_distance == float('inf'):
        return -1

    return min_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
