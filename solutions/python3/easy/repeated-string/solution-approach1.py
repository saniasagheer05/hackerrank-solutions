# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
# Problem     Repeated String
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 12:27 a.m.
# Technique   modular-arithmetic-string-counting
# Time        O(L) where L is the length of string s
# Space       O(L) to store the slice of the string
# Insight     The total count of 'a' is derived by multiplying the frequency of 'a' in the base string by the number of full repetitions and adding the count from the remaining prefix.
# Interview   Before: "I would iterate through the string n times to count 'a'." After: "That would be O(n) and fail for large n. Instead, I calculate the count in O(L) time by using modular arithmetic to determine full cycles and the remaining substring length, which handles n up to 10^12 efficiently."
# Pitfalls    (1) Failing to account for the remainder of n divided by the length of s.  (2) Assuming n is always smaller than the length of s, which contradicts the constraints.  (3) Using an iterative loop to build the string up to length n, which causes memory overflow for large n.
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
