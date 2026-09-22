# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
# Problem     Breaking the Records
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:49 p.m.
# ──────────────────────────────────────────────────

def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]

    max_count = 0
    min_count = 0

    for score in scores[1:]:
        if score > highest:
            highest = score
            max_count += 1

        if score < lowest:
            lowest = score
            min_count += 1

    return [max_count, min_count]


n = int(input())
scores = list(map(int, input().split()))

result = breakingRecords(scores)
print(result[0], result[1])
