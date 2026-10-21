# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# Problem     Encryption
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-22, 12:08 a.m.
# Technique   grid-column-traversal
# Time        O(L)
# Space       O(L)
# Insight     The algorithm calculates grid dimensions based on the square root of the string length and extracts characters column-wise to form the encrypted message.
# Interview   Before: "How would you map a linear string into a 2D grid for column-based encryption?" After: "I remove spaces and determine dimensions using floor and ceil of the square root, ensuring rows times columns covers the length. This O(L) approach iterates through columns to collect characters, handling the grid bounds with index checks."
# Pitfalls    (1) Failing to handle the case where rows times columns is less than the string length by incrementing rows.  (2) Incorrectly calculating the index as row times rows instead of row times columns during column traversal.  (3) Including spaces in the string length calculation, which violates the requirement to remove them first.
# ──────────────────────────────────────────────────


import math

def encryption(s):
    s = s.replace(" ", "")
    n = len(s)

    rows = math.floor(math.sqrt(n))
    cols = math.ceil(math.sqrt(n))

    if rows * cols < n:
        rows += 1

    result = []

    for col in range(cols):
        word = ""
        for row in range(rows):
            index = row * cols + col
            if index < n:
                word += s[index]
        result.append(word)

    return " ".join(result)


if __name__ == '__main__':
    s = input()
    print(encryption(s))
