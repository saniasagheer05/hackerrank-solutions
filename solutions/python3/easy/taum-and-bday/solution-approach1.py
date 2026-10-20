# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true
# Problem     Taum and B'day
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-21, 12:15 a.m.
# ──────────────────────────────────────────────────



def taumBday(b, w, bc, wc, z):
    black_cost = min(bc, wc + z)
    white_cost = min(wc, bc + z)

    return b * black_cost + w * white_cost


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        b, w = map(int, input().split())
        bc, wc, z = map(int, input().split())

        result = taumBday(b, w, bc, wc, z)
        print(result)
