# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true
# Problem     HackerRank in a String!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 11:26 p.m.
# ──────────────────────────────────────────────────

def hackerrankInString(s):
    target = "hackerrank"
    j = 0

    for char in s:
        if j < len(target) and char == target[j]:
            j += 1

    return "YES" if j == len(target) else "NO"


q = int(input())

for _ in range(q):
    s = input()
    print(hackerrankInString(s))
