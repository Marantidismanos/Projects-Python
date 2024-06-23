student_heights = input().split()

for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
max=0
print(f"This is the list : {student_heights} \n")
for i in student_heights:
    if i> max:
        max=i

print(f"The highest score in the class is : {max} \n")


