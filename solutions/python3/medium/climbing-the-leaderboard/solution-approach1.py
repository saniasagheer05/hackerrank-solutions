# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# Problem     Climbing the Leaderboard
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-04, 11:56 p.m.
# ──────────────────────────────────────────────────

def climbingLeaderboard(ranked, player):
   
    unique = []
    for score in ranked:
        if not unique or unique[-1] != score:
            unique.append(score)

    result = []
    i = len(unique) - 1

    for score in player:
        while i >= 0 and score >= unique[i]:
            i -= 1

        result.append(i + 2)

    return result


n = int(input())
ranked = list(map(int, input().split()))

m = int(input())
player = list(map(int, input().split()))

result = climbingLeaderboard(ranked, player)

for rank in result:
    print(rank)
