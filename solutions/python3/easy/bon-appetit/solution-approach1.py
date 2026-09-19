# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# Problem     Bill Division
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-20, 02:01 a.m.
# Technique   sum-subtraction-comparison
# Time        O(n)
# Space       O(1)
# Insight     The algorithm calculates the fair share by subtracting the item at index k from the total sum and dividing by two, then compares this result against the charged amount.
# Interview   Before: "I could iterate through the list and sum everything except index k." After: "Summing the entire list and subtracting the specific item at index k is more efficient, achieving O(n) time and O(1) space complexity while correctly handling the zero-based index k."
# Pitfalls    (1) Incorrectly assuming the division by two might result in a float, though the problem guarantees the result is always an integer.  (2) Failing to account for the zero-based index k when subtracting the item Anna did not eat from the total bill sum.
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
