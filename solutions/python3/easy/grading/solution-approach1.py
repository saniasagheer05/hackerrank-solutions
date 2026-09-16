# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Problem     Grading Students
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:14 a.m.
# Technique   linear-scan-conditional-rounding
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through each grade, applying the rounding rule only if the grade is at least 38 and the difference to the next multiple of five is strictly less than three.
# Interview   Before: "How would you implement the rounding logic for student grades?" After: "I iterate through the list in O(n) time, checking if the grade is at least 38 and if the difference to the next multiple of five is less than three, ensuring we only round when the policy permits."
# Pitfalls    (1) Failing to account for the rule that grades below 38 must not be rounded.  (2) Incorrectly rounding grades where the difference to the next multiple of five is exactly 3.  (3) Miscalculating the next multiple of five by using incorrect integer division logic.
# ──────────────────────────────────────────────────

def gradingStudents(grades):
    result = []

    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5

            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)

    return result


n = int(input())

grades = []
for _ in range(n):
    grades.append(int(input()))

for grade in gradingStudents(grades):
    print(grade)
