# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
# Problem     Breaking the Records
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 11:49 p.m.
# Technique   linear-scan-tracking-extremes
# Time        O(n)
# Space       O(1)
# Insight     The algorithm initializes the record-tracking variables with the first game score and iterates through the remaining scores to update the counts whenever a new maximum or minimum is encountered.
# Interview   Before: "I would use two separate variables to track the current max and min, updating them as I iterate through the list." After: "I implemented a linear O(n) scan that compares each subsequent score against the initial record, ensuring we only count strictly better or worse performances."
# Pitfalls    (1) Failing to initialize the records with the first game score, which leads to incorrect counts if the first score is not the global minimum or maximum.  (2) Using non-strict inequality operators instead of strict ones, which violates the requirement that a record is only broken if the score is strictly greater or lesser.
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
