# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true
# Problem     Luck Balance
# Difficulty  Easy
# Subdomain   Greedy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:58 p.m.
# Technique   greedy-sorting-important-contests
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm maximizes luck by losing all unimportant contests and the k largest important contests, while winning the remaining important contests to minimize the luck penalty.
# Interview   Before: "I would iterate through all contests and track the total luck." After: "I separate important contests, sort them descending, and greedily choose to lose the k largest ones to maximize luck in O(N log N) time, ensuring the constraint on important contest losses is satisfied."
# Pitfalls    (1) Failing to account for the requirement that Lena must win the smallest important contests if the total count of important contests exceeds k.  (2) Incorrectly assuming that all important contests should be lost, which violates the constraint that Lena can lose no more than k important contests.  (3) Misinterpreting the luck balance calculation by adding instead of subtracting the luck value when Lena is forced to win an important contest.
# ──────────────────────────────────────────────────

def luckBalance(k, contests):
    important = []
    luck = 0

    for amount, importance in contests:
        if importance == 0:
            luck += amount
        else:
            important.append(amount)

    important.sort(reverse=True)

    for i in range(len(important)):
        if i < k:
            luck += important[i]
        else:
            luck -= important[i]

    return luck


n, k = map(int, input().split())

contests = []

for _ in range(n):
    contests.append(list(map(int, input().split())))

answer = luckBalance(k, contests)

print(answer)
