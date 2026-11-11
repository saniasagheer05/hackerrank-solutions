# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
# Problem     Beautiful Triplets
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 01:24 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)

    for num in arr:
        if num + d in arr_set and num + 2 * d in arr_set:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
