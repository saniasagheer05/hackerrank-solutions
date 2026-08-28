# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 11:49 p.m.
# ──────────────────────────────────────────────────

def camelcase(s):
    count = 1  

    for char in s:
        if char.isupper():
            count += 1

    return count


s = input().strip()
print(camelcase(s))
