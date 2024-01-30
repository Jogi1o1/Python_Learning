# You are going to write a program that calculates the average student height from a List of heights.
# Here storing the input from the user in a variable
student_heights = input("Please provide the heights of the students separated by spaces\n").split()
sum_heights = 0
for  i in range(0,len(student_heights)) :
  student_heights[i] = int(student_heights[i])
  sum_heights += student_heights[i]

print(f"The sum of the heights of the students is {sum_heights} cms")
print(f"total number of students is {i+1}")
average_height = int(sum_heights/(i+1))
print(f"the average height of students is {average_height} cms")

  
    
