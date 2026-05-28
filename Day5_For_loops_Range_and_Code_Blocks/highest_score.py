student_scores = [
    92, 85, 78, 95, 64, 88, 72, 91, 83, 60,
    77, 94, 85, 55, 81, 99, 84, 76, 45, 89,
    92, 73, 68, 85, 88, 93, 70, 82, 79, 66
]
total_exam_scores = sum(student_scores)
print(total_exam_scores)

best_scores = max(student_scores)
print(best_scores)

max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)