# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
# Problem     Plus Minus
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:28 p.m.
# Technique   linear-scan-counter
# Time        O(n)
# Space       O(1)
# Insight     The algorithm iterates through the array once to count occurrences of positive, negative, and zero values, then calculates their respective ratios relative to the total array length.
# Interview   Before: "I will use a hash map to store counts." After: "A simple linear scan with three counters is more efficient, achieving O(n) time and O(1) space, which is optimal for this problem."
# Pitfalls    (1) Failure to format the output to exactly six decimal places as required by the problem statement.  (2) Integer division in languages other than Python might truncate the result to zero before floating-point conversion.
# ──────────────────────────────────────────────────



import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    n = len(arr)

    print("{:.6f}".format(positive / n))
    print("{:.6f}".format(negative / n))
    print("{:.6f}".format(zero / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
