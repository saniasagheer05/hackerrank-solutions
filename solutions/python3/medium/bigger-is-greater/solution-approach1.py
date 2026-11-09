# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
# Problem     Bigger is Greater
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 09:08 p.m.
# ──────────────────────────────────────────────────


import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    chars = list(w)
    n = len(chars)

    i = n - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    j = n - 1
    while chars[j] <= chars[i]:
        j -= 1

    chars[i], chars[j] = chars[j], chars[i]

    chars[i + 1:] = reversed(chars[i + 1:])

    return ''.join(chars)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')

    fptr.close()
