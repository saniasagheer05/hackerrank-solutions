# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# Problem     Climbing the Leaderboard
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-04, 11:56 p.m.
# Technique   unique-list-two-pointers
# Time        O(n + m)
# Space       O(n)
# Insight     The algorithm reduces the leaderboard to unique scores and uses a pointer that traverses the unique list in reverse to determine the rank for each ascending player score.
# Interview   Before: "I would use binary search for each player score." After: "Since player scores are ascending, I can use a two-pointer approach to achieve O(n + m) time complexity, which is more efficient than repeated binary searches."
# Pitfalls    (1) Failing to handle duplicate scores in the leaderboard, which violates the dense ranking rule.  (2) Incorrectly calculating the rank index when the player score exceeds all existing leaderboard scores.  (3) Assuming the leaderboard is already unique, which contradicts the problem statement's example.
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
