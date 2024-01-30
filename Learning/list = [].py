list = []
N = int(input("Enter the count of numbers :"))
print("Please enter the desired numbers\n")
for i in range (0,N):
    Var = int(input())
    list.append(Var) 
for j in range (0, N):
    cube = list(j)
    New =+ cube
user_num = int(input("Enter the number you want to compare"))
if New == user_num:
    print("True")
else :
    print("False")