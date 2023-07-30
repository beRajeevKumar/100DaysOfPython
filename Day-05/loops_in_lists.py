# fruits = ["Apple", "Banana", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# Exercise 1 - Average Height
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])


# height_sum = 0
# count = 0
# for heights in student_heights:
#     count += 1
#     height_sum += heights
# avg_height = height_sum/count
# print(round(avg_height))


# Exercise 2 - High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for student_score in student_scores:
    if max < student_score:
        max = student_score
print(f"The highest score in the class is: {max}")
