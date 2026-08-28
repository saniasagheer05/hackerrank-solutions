# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
# Problem     Two Characters
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 11:52 p.m.
# Technique   brute-force-character-pair-filtering
# Time        O(C^2 * N)
# Space       O(N)
# Insight     The algorithm iterates through every unique pair of characters in the string, filters the original string to retain only those two characters, and validates if they alternate.
# Interview   Before: "I would use a frequency map to count occurrences." After: "Since we need alternating patterns, I iterate through all O(C^2) character pairs and validate the O(N) filtered string, resulting in O(C^2 * N) time complexity where C is the alphabet size."
# Pitfalls    (1) Failing to handle cases where no valid alternating string can be formed, which must return 0.  (2) Assuming that any two characters will form a valid alternating string without checking for consecutive duplicates.  (3) Neglecting the requirement that all instances of removed characters must be excluded from the final string.
# ──────────────────────────────────────────────────

def alternate(s):
    chars = list(set(s))
    max_len = 0

    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            a = chars[i]
            b = chars[j]

            temp = ""

        
            for ch in s:
                if ch == a or ch == b:
                    temp += ch

            
            valid = True
            for k in range(1, len(temp)):
                if temp[k] == temp[k - 1]:
                    valid = False
                    break

            if valid:
                max_len = max(max_len, len(temp))

    return max_len


n = int(input())
s = input()

print(alternate(s))
