# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
# Problem     Between Two Sets
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 01:59 a.m.
# Technique   brute-force-range-scan
# Time        O(100 * (n + m))
# Space       O(1)
# Insight     The algorithm iterates through all integers from 1 to 100, verifying if each candidate is a multiple of all elements in array a and a factor of all elements in array b.
# Interview   Before: "I could calculate the LCM of a and GCD of b to narrow the search space." After: "Given the constraints where elements are at most 100, a brute-force scan from 1 to 100 is O(100 * (n + m)), which is efficient and avoids complex number theory logic."
# Pitfalls    (1) Assuming the search range must be dynamic based on array values rather than the problem constraint of 100.  (2) Failing to check both conditions for every candidate integer in the range.  (3) Incorrectly handling the modulo operator when checking if elements of a are factors of the candidate or if the candidate is a factor of elements in b.
# ──────────────────────────────────────────────────

def getTotalX(a, b):
    count = 0

    for num in range(1, 101):
        valid_a = True
        valid_b = True

        for x in a:
            if num % x != 0:
                valid_a = False
                break

        for x in b:
            if x % num != 0:
                valid_b = False
                break

        if valid_a and valid_b:
            count += 1

    return count


if __name__ == '__main__':
    first = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(getTotalX(a, b))
