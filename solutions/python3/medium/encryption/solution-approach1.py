# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# Problem     Encryption
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-22, 12:08 a.m.
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
