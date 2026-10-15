# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
# Problem     Cut the sticks
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:29 p.m.
# Technique   iterative-list-filtering
# Time        O(n^2)
# Space       O(n)
# Insight     The algorithm repeatedly records the current list size and filters out all elements equal to the minimum value until the list becomes empty.
# Interview   Before: "How would you simulate the stick cutting process?" After: "I used a list comprehension to filter out the shortest sticks in each iteration. This results in O(n^2) time complexity, which is efficient enough given the constraint n <= 1000."
# Pitfalls    (1) Failing to account for the O(n^2) complexity when n is large, as the list comprehension iterates over the remaining sticks in every step.  (2) Misinterpreting the requirement to discard all sticks of the shortest length, which is handled by the filter condition stick > shortest.
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
