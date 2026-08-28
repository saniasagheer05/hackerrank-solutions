# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true
# Problem     CamelCase
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 11:49 p.m.
# Technique   isupper-scan
# Time        O(n)
# Space       O(1)
# Insight     The algorithm counts the number of words by initializing the count to one and incrementing it for every uppercase character encountered in the string.
# Interview   Before: "I could split the string by uppercase letters using regex." After: "Since the first word is always lowercase, I simply count the uppercase letters and add one. This approach runs in O(n) time and O(1) space, which is optimal for a single pass."
# Pitfalls    (1) Failing to account for the first word, which is always lowercase and does not contain an uppercase letter.  (2) Assuming the input string could be empty, which contradicts the problem statement requiring at least one word.
# ──────────────────────────────────────────────────

def camelcase(s):
    count = 1  

    for char in s:
        if char.isupper():
            count += 1

    return count


s = input().strip()
print(camelcase(s))
