# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# Problem     Append and Delete
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 12:33 a.m.
# Technique   common-prefix-length-calculation
# Time        O(min(len(s), len(t)))
# Space       O(1)
# Insight     The algorithm calculates the minimum operations required by identifying the common prefix length and then verifies if the remaining budget allows for the transformation given the parity constraint.
# Interview   Before: "I would simulate the operations step-by-step." After: "That is inefficient for large k. Instead, calculate the common prefix length to find the minimum operations needed, then check if the remaining k is non-negative, even, or large enough to clear the entire string in O(min(len(s), len(t))) time."
# Pitfalls    (1) Failing to account for the case where k is large enough to delete the entire string and then perform redundant deletions on an empty string.  (2) Ignoring the parity requirement where the difference between k and the minimum operations must be even to allow for back-and-forth deletions.  (3) Miscalculating the minimum operations as simply the difference in lengths rather than accounting for the shared prefix.
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
