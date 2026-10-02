# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
# Problem     Designer PDF Viewer
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:32 p.m.
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
