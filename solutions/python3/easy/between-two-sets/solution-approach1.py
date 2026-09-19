# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
# Problem     Between Two Sets
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 01:59 a.m.
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
