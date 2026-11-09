# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
# Problem     Bigger is Greater
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 09:08 p.m.
# Technique   next-lexicographical-permutation
# Time        O(N)
# Space       O(N)
# Insight     The algorithm identifies the rightmost character that is smaller than its successor, swaps it with the smallest character to its right that is larger, and reverses the remaining suffix to achieve the smallest lexicographical increase.
# Interview   Before: "How would you find the next permutation of a string?" After: "I scan from right to left to find the first decreasing pair, swap the pivot with its successor's smallest greater element, and reverse the suffix. This runs in O(N) time and O(N) space, handling cases like 'no answer' when the string is non-increasing."
# Pitfalls    (1) Failing to handle the case where the entire string is in descending order, which requires returning 'no answer'.  (2) Incorrectly reversing the suffix after the swap, which prevents the result from being the smallest possible lexicographical increase.  (3) Using an incorrect loop condition for finding the pivot, such as failing to account for equal characters.
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
