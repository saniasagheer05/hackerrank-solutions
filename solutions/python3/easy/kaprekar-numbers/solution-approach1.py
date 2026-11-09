# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
# Problem     Modified Kaprekar Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 09:09 p.m.
# ──────────────────────────────────────────────────


import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    result = []

    for i in range(p, q + 1):
        square = i * i
        s = str(square)

        d = len(str(i))

        left = s[:-d] if len(s) > d else "0"
        right = s[-d:]

        left = int(left) if left else 0
        right = int(right)

        if left + right == i:
            result.append(str(i))

    if result:
        print(" ".join(result))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())

    kaprekarNumbers(p, q)
