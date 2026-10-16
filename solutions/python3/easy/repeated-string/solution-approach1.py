# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
# Problem     Repeated String
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 12:27 a.m.
# ──────────────────────────────────────────────────


def repeatedString(s, n):
    count_a = s.count('a')
    full_repeats = n // len(s)
    remaining = n % len(s)

    total = count_a * full_repeats
    total += s[:remaining].count('a')

    return total


if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())

    print(repeatedString(s, n))
