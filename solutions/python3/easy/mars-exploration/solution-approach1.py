# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true
# Problem     Mars Exploration
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 11:28 p.m.
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
