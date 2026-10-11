# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# Problem     Append and Delete
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 12:33 a.m.
# ──────────────────────────────────────────────────


def appendAndDelete(s, t, k):
    i = 0

    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1

    operations = (len(s) - i) + (len(t) - i)

    if k >= len(s) + len(t):
        return "Yes"

    if operations <= k and (k - operations) % 2 == 0:
        return "Yes"

    return "No"


s = input().strip()
t = input().strip()
k = int(input().strip())

print(appendAndDelete(s, t, k))
