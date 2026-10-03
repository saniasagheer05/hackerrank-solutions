# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
# Problem     Angry Professor
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-03, 11:32 p.m.
# Technique   linear-scan-counter
# Time        O(n)
# Space       O(1)
# Insight     The algorithm determines if the class is cancelled by counting the number of students who arrived at or before time zero and comparing that total against the threshold k.
# Interview   Before: "I would sort the arrival times to find the cutoff point." After: "Sorting is unnecessary because we only need to count non-positive values. This linear scan approach runs in O(n) time and O(1) space, correctly handling the threshold k as defined in the problem statement."
# Pitfalls    (1) Confusing the threshold k with the number of students n, leading to incorrect comparison logic.  (2) Misinterpreting the arrival time condition, specifically failing to include zero as an on-time arrival (a[i] <= 0).  (3) Returning the wrong string value, as the problem requires YES for cancellation and NO for proceeding.
# ──────────────────────────────────────────────────

def angryProfessor(k, a):
    count = 0

    for x in a:
        if x <= 0:
            count += 1

    if count < k:
        return "YES"
    else:
        return "NO"


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(angryProfessor(k, a))
