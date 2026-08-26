# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
# Problem     Mini-Max Sum
# Difficulty  Easy
# Subdomain   Warmup
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-27, 12:37 a.m.
# Technique   total-sum-subtraction
# Time        O(n)
# Space       O(1)
# Insight     The minimum sum is the total sum minus the maximum element, and the maximum sum is the total sum minus the minimum element.
# Interview   Before: "I could sort the array and sum the first four or last four elements." After: "Sorting takes O(n log n), but calculating the total sum and subtracting the min or max element achieves the same result in O(n) time, which is more efficient for this fixed-size input."
# Pitfalls    (1) Failing to use 64-bit integers for the sum calculation, which risks integer overflow as noted in the problem constraints.  (2) Assuming the input array is sorted, which is not guaranteed by the problem statement.
# ──────────────────────────────────────────────────

arr = list(map(int, input().split()))

total = sum(arr)

minimum = total - max(arr)
maximum = total - min(arr)

print(minimum, maximum)
