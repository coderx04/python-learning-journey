
student_scores = [150, 142, 1850, 1 ,120, 171, 184, 149, 24, 0, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

lowest_score = 0

for i in student_scores:
    lowest_score = i
    for i in student_scores:
        if i < lowest_score:
            lowest_score = i

print(lowest_score)

highest_score = 0

for i in student_scores:
    if i > highest_score:
        highest_score = i

print(highest_score)
