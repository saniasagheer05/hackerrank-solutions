# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
# Problem     Designer PDF Viewer
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:32 p.m.
# Technique   linear-scan-max-tracking
# Time        O(n)
# Space       O(1)
# Insight     The algorithm calculates the highlighted area by identifying the maximum height among all characters in the word and multiplying it by the word's length.
# Interview   Before: "I would iterate through the string and store each character's height in a hash map to find the maximum." After: "Since the alphabet is fixed, I can map characters to indices using ord(char) - ord('a') to find the maximum height in O(n) time, where n is the word length."
# Pitfalls    (1) Incorrectly calculating the character index by failing to subtract the ASCII value of 'a'.  (2) Assuming the input word contains uppercase letters, which violates the problem constraint that the word consists only of lowercase English alphabetic letters.
# ──────────────────────────────────────────────────

def designerPdfViewer(h, word):
    max_height = 0

    for char in word:
        index = ord(char) - ord('a')
        if h[index] > max_height:
            max_height = h[index]

    return max_height * len(word)


# Read input
h = list(map(int, input().split()))
word = input().strip()

print(designerPdfViewer(h, word))
