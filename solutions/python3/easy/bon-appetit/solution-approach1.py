# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# Problem     Bill Division
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 02:01 a.m.
# ──────────────────────────────────────────────────

def bonAppetit(bill, k, b):
    total = sum(bill)
    total -= bill[k]
    anna = total // 2

    if b > anna:
        print(b - anna)
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
