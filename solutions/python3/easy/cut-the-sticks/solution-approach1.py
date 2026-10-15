# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
# Problem     Cut the sticks
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:29 p.m.
# ──────────────────────────────────────────────────


def cutTheSticks(arr):
    result = []

    while arr:
        result.append(len(arr))
        shortest = min(arr)
        arr = [stick for stick in arr if stick > shortest]

    return result


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
