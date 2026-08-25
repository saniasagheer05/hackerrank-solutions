# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
# Problem     Simple Array Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:59 p.m.
# Technique   built-in-sum-function
# Time        O(n)
# Space       O(1)
# Insight     The implementation utilizes the language's native summation function to aggregate all integer elements within the provided list.
# Interview   Before: "I should iterate through the array and maintain a running total variable." After: "Using the built-in sum function is more idiomatic and efficient, achieving O(n) time complexity while handling the array of size n provided in the input."
# Pitfalls    (1) Assuming the input array might be empty when the problem constraints imply n is at least 1.  (2) Overcomplicating the solution with manual loops when a standard library function is available.
# ──────────────────────────────────────────────────

def simpleArraySum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))

print(simpleArraySum(ar))
