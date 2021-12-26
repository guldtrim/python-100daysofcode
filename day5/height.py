student_heights = input("Input a list of student heights ").split()
total_value = 0
amount_of_students = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_value += student_heights[n]
  amount_of_students += 1

calculation = total_value / amount_of_students
print(round(calculation))
