student_heights = input().split()

for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])

print(student_heights)

total_height=0
for height in student_heights:
    total_height+=height

print(f"Total height = {total_height}")
num_of_std=len(student_heights)
print(f"Number of students = {num_of_std}")
avg_height=total_height/num_of_std
print(f"Average height = {avg_height}")
