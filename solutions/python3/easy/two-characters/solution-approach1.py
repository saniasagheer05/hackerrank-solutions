# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
# Problem     Two Characters
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 11:52 p.m.
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
