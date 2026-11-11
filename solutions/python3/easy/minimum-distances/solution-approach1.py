# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
# Problem     Minimum Distances
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 01:27 a.m.
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
