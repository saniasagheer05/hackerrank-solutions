# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true
# Problem     HackerRank in a String!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 11:26 p.m.
# Technique   single-pointer-subsequence-scan
# Time        O(n)
# Space       O(1)
# Insight     The algorithm maintains a pointer to the target string and advances it only when the current character in the input string matches the character at the pointer's position.
# Interview   Before: I would use a frequency map to count characters. After: Since order matters, I use a single pointer to track the subsequence progress in O(n) time, ensuring we find all characters of 'hackerrank' in sequence.
# Pitfalls    (1) Failing to check if the pointer j has reached the end of the target string before accessing target[j].  (2) Returning YES prematurely if the target string is found before the end of the input string s.
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
