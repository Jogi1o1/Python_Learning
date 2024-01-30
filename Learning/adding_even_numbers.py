# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100
# taking input from the user of the limit number
limits = input("please provide the starting range and end range of the limit through which you want to calculate the sum of even numbers? they should be separated by space.\n").split()
# limit = int(limits)
# if limit[1] <= 1000 :
#     if limit[0] < limit[1]:
#         if limit[0] % 2 == 0 :
#           i = limit[0]
#           for i in range(limit[0],limit[1]+1):
#             i += limit[i]
#         else :
#           i = limit[0] + 1
#           for i in range(limit[0]+1,limit[1]+1):
#             i += limit[i]
#     else :
#         print("Starting number should be smaller than the ending number")  
# else : 
#     print("Range should be less than 1000")

sum = 0
for i in range(int(limits[0]), int(limits[1])+1):
   if i % 2 == 0 :
      sum+=i
print(sum)

