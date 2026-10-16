# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# Problem     Non-Divisible Subset
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 12:24 a.m.
# ──────────────────────────────────────────────────


def nonDivisibleSubset(k, s):
    remainder_count = [0] * k

    for num in s:
        remainder_count[num % k] += 1

    count = min(remainder_count[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += max(remainder_count[i], remainder_count[k - i])
        else:
            count += min(remainder_count[i], 1)

    return count


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    print(nonDivisibleSubset(k, s))
