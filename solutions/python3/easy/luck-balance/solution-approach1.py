# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true
# Problem     Luck Balance
# Difficulty  Easy
# Subdomain   Greedy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:58 p.m.
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
