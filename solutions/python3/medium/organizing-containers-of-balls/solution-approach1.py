# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
# Problem     Organizing Containers of Balls
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-22, 12:07 a.m.
# ──────────────────────────────────────────────────


def organizingContainers(container):
    n = len(container)

    container_capacity = sorted(sum(row) for row in container)

    ball_types = sorted(
        sum(container[i][j] for i in range(n))
        for j in range(n)
    )

    return "Possible" if container_capacity == ball_types else "Impossible"


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())

        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)
