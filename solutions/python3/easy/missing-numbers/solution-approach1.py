# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
# Problem     Missing Numbers
# Difficulty  Easy
# Subdomain   Search
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-09, 08:06 p.m.
# ──────────────────────────────────────────────────

from collections import Counter

def missingNumbers(arr, brr):
    count_arr = Counter(arr)
    count_brr = Counter(brr)

    result = []

    for num in count_brr:
        if count_brr[num] > count_arr[num]:
            result.append(num)

    return sorted(result)


n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

answer = missingNumbers(arr, brr)

print(*answer)
