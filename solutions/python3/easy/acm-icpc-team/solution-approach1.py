# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# Problem     ACM ICPC Team
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 01:40 p.m.
# Technique   nested-loop-bit-comparison
# Time        O(n^2 * m)
# Space       O(1)
# Insight     The algorithm iterates through all unique pairs of attendees and computes the bitwise OR of their topic strings to determine the total number of known subjects.
# Interview   Before: "I would use a hash map to count topic frequencies." After: "Since we need to compare every pair of attendees, an O(n^2 * m) approach is necessary to check all combinations, where n is the number of attendees and m is the number of topics."
# Pitfalls    (1) Failing to initialize the max_topics counter to zero, which would cause incorrect results if all teams know zero topics.  (2) Using an incorrect inner loop range for j, which must start at i + 1 to avoid comparing an attendee with themselves or counting the same pair twice.  (3) Assuming bitwise operations on strings are faster than manual character comparison, which is not necessarily true in Python without converting to integers.
# ──────────────────────────────────────────────────


def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    teams = 0

    for i in range(n):
        for j in range(i + 1, n):
            count = 0

            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    count += 1

            if count > max_topics:
                max_topics = count
                teams = 1
            elif count == max_topics:
                teams += 1

    return [max_topics, teams]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input().strip()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result[0])
    print(result[1])
