# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
# Problem     Viral Advertising
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 08:08 p.m.
# Technique   iterative-simulation
# Time        O(n)
# Space       O(1)
# Insight     The cumulative number of likes is calculated by iteratively updating the number of people who share the advertisement based on the floor division of the previous day's recipients.
# Interview   Before: "I would use a recursive approach to track the daily likes." After: "An iterative simulation is more efficient here, achieving O(n) time and O(1) space complexity, which is optimal given the constraints on n."
# Pitfalls    (1) Confusing the number of people who share the advertisement with the number of people who like it.  (2) Failing to apply integer division correctly when calculating the number of likes per day.  (3) Misinterpreting the cumulative sum requirement by returning only the likes from the final day instead of the total.
# ──────────────────────────────────────────────────

def viralAdvertising(n):
    shared = 5
    total_likes = 0

    for day in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3

    return total_likes


n = int(input())
print(viralAdvertising(n))
