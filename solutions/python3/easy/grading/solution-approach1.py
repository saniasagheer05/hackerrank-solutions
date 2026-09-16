# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Problem     Grading Students
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:14 a.m.
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
