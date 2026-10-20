# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# Problem     ACM ICPC Team
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 01:40 p.m.
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
