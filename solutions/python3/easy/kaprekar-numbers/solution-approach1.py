# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
# Problem     Modified Kaprekar Numbers
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 09:09 p.m.
# Technique   string-splitting-square-sum
# Time        O((q-p) * log10(q^2))
# Space       O(q-p)
# Insight     The algorithm validates a modified Kaprekar number by squaring the integer, partitioning the resulting string into two segments based on the original digit count, and verifying if their sum equals the original value.
# Interview   Before: "How do I handle the split when the square has fewer digits than expected?" After: "The code handles this by using string slicing and defaulting the left part to zero, ensuring O(N log(N^2)) complexity where N is the range size, correctly identifying numbers like 1 and 9."
# Pitfalls    (1) Failing to handle the case where the left substring is empty by defaulting it to zero as required by the modified Kaprekar definition.  (2) Incorrectly calculating the split point by using the square's length instead of the original number's digit count.  (3) Assuming the right part must be non-zero, which contradicts the requirement that r may contain leading zeros.
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
