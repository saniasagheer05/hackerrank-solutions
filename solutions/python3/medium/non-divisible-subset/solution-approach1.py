# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# Problem     Non-Divisible Subset
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 12:25 a.m.
# Technique   remainder-frequency-counting
# Time        O(n + k)
# Space       O(k)
# Insight     The algorithm groups integers by their remainder modulo k and greedily selects the larger frequency between complementary remainder pairs to maximize the subset size while avoiding sums divisible by k.
# Interview   Before: "I could try generating all subsets and checking each one." After: "That would be exponential. Instead, I use a frequency array of size k to count remainders, achieving O(n + k) time complexity, which is optimal given the constraints on n and k."
# Pitfalls    (1) Failing to handle the remainder 0 case by capping its contribution at 1, as multiple numbers with remainder 0 sum to a multiple of k.  (2) Incorrectly handling the middle element when k is even, where the remainder k/2 must also be capped at 1 to avoid self-sum divisibility.  (3) Using an incorrect loop range that misses the boundary condition at k/2, leading to an incomplete count of valid remainder pairs.
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
