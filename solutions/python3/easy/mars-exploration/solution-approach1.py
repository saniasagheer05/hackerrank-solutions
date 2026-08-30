# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true
# Problem     Mars Exploration
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 11:28 p.m.
# Technique   string-pattern-comparison
# Time        O(n)
# Space       O(n)
# Insight     The algorithm constructs an expected SOS sequence of equal length to the input and counts character mismatches at each index.
# Interview   Before: "I would compare the string against a repeating SOS pattern." After: "I implemented a linear O(n) scan that compares the input against a generated SOS string, ensuring the total length matches the input constraints."
# Pitfalls    (1) Assuming the input length is always a multiple of three, though the problem constraints imply valid SOS transmissions.  (2) Creating an unnecessarily large string in memory if the input length is extremely high, which could impact space complexity.
# ──────────────────────────────────────────────────

def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    count = 0

    for i in range(len(s)):
        if s[i] != expected[i]:
            count += 1

    return count


s = input().strip()
print(marsExploration(s))
