# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
# Problem     Forming a Magic Square
# Difficulty  Medium
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-01, 09:23 p.m.
# ──────────────────────────────────────────────────

def formingMagicSquare(s):
    magic_squares = [
        [[8, 1, 6],
         [3, 5, 7],
         [4, 9, 2]],

        [[6, 1, 8],
         [7, 5, 3],
         [2, 9, 4]],

        [[4, 9, 2],
         [3, 5, 7],
         [8, 1, 6]],

        [[2, 9, 4],
         [7, 5, 3],
         [6, 1, 8]],

        [[8, 3, 4],
         [1, 5, 9],
         [6, 7, 2]],

        [[4, 3, 8],
         [9, 5, 1],
         [2, 7, 6]],

        [[6, 7, 2],
         [1, 5, 9],
         [8, 3, 4]],

        [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]]
    ]

    minimum_cost = float('inf')

    for magic in magic_squares:
        cost = 0

        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])

        minimum_cost = min(minimum_cost, cost)

    return minimum_cost


# Read the 3 rows
s = []

for _ in range(3):
    s.append(list(map(int, input().split())))

# Print the answer
print(formingMagicSquare(s))
