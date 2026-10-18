# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
# Problem     Queen's Attack II
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 12:15 a.m.
# Technique   directional-ray-casting-with-set
# Time        O(k + n)
# Space       O(k)
# Insight     The algorithm calculates the maximum possible distance in each of the eight directions and then reduces those distances by checking for obstacles along each ray.
# Interview   Before: "I would iterate through every cell on the board to check if the queen can attack it." After: "That is inefficient for large boards. Instead, I calculate the maximum distance in each of the eight directions and subtract the distance to the nearest obstacle, resulting in O(k + n) time complexity."
# Pitfalls    (1) Failing to account for the 1-based indexing of the chessboard, which can lead to incorrect distance calculations.  (2) Assuming obstacles are sorted, which is not guaranteed by the problem statement and would break the logic if relied upon.  (3) Neglecting to handle the case where multiple obstacles exist on the same ray, which the code correctly manages by breaking at the first encountered obstacle.
# ──────────────────────────────────────────────────


def queensAttack(n, k, r_q, c_q, obstacles):

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]


    distances = [
        n - r_q, r_q - 1, n - c_q, c_q - 1,
        min(n - r_q, n - c_q),
        min(n - r_q, c_q - 1),
        min(r_q - 1, n - c_q),
        min(r_q - 1, c_q - 1)
    ]

    obstacle_set = set(map(tuple, obstacles))

    result = 0

    for i, (dr, dc) in enumerate(directions):
        for step in range(1, distances[i] + 1):
            r = r_q + dr * step
            c = c_q + dc * step

            if (r, c) in obstacle_set:
                distances[i] = step - 1
                break

        result += distances[i]

    return result


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    r_q, c_q = map(int, input().rstrip().split())

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
