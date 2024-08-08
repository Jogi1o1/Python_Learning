# name = input("Enter your first name : \n")
# print("The length of your first name is : "+str(len(name)))

# strings = "Jogi$Singh$"
# print(strings.count("$"))

# num1 = input("Enter your first num")
# num2 = input("Enter your second num")
# num3 = input("Enter your third num")

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is greater")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is greater")
# else :
#     print(f"{num3} is greater")

# num = int(input("Please enter the number you want to check? \n"))
# if num%7==0:
#     print(f"{num} is a multiple of 7")
# else :
#     print(f"{num} is not a multiple of 7")

# lists = []
# for i in range(3):
#     movie = input("Enter your fav movie\n")
#     lists.append(movie.capitalize())
# print(f" your fav movies are {lists}")

# lists = [1,2,3,2,1,2]
# palindromes = True
# for i in range(len(lists)):
#     if lists[i]==lists[-(i+1)]:
#         continue
#     else:
#         palindromes = False
#         break

# print(f"Provide list is palindrome : {palindromes}")

# lists = [1,2,3,2,1]
# lists1 = lists.copy()
# lists1.reverse()
# print(lists1)
# if lists == lists1:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# tup = ("C","D","A","A","B","B","A")
# print(f"The total num of A's are : {tup.count('A')}")

# lists = []
# for i in range(len(tup)):
#     lists.append(tup[i])
# lists.sort()
# print(lists)

# dict = {}
# dict.update({
#     "table" : ["a piece of furniture","list of facts & figures"],
#     "cat" : "a small animal"
# })
# print(dict)

# set1 = set()
# set1.update(
#     {
#         "python",
#         "java",
#         "C++",
#         "python",
#         "javascript",
#         "java",
#         "python",
#         "java",
#         "C++",
#         "C"
#     }
# )
# print(len(set1))

# set1 = {("int",9),("float",9.0)}
# print(set1)

# i = 1
# while i<=100:
#     print(i)
#     i += 1

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# i = 1
# num = int(input("Please provide the number you want to get the multiplcation table of"))
# while i <= 10:
#     print(f"{num} X {i} = {i*num}")
#     i += 1

# list1 = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

# tup1 = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# num = int(input("Enter the number you want to search"))
# num_found = False
# while i < len(tup1):
#     if num == tup1[i]:
#         num_found = True
#         break
#     i += 1
# print(f"Number found in tuple = {num_found}")

# tup1 = (1,4,9,16,25,36,49,64,81,100)
# for el in tup1:
#     print(el)

# list1 = [1,4,9,16,25,36,49,64,81,100]
# for l in list1:
#     print(l)

# tup1 = (1,4,9,16,25,36,49,64,81,100)
# num = int(input("Enter the number you want to search"))
# for i in tup1:
#     if num == i:
#         print("Number found")
#         break
# else:
#     print("Not found")

# for i in range(100,0,-1):
#     print(i)

# num = int(input("Enter the number you want to get table of"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# num = int(input("Enter the number to which you want to calculate the sum"))
# i = 0
# sum = 0
# while i <= num :
#     sum = sum + i
#     i += 1
# print(sum)

# num = int(input("enter the number you want to calculate factorial of"))
# fact = 1
# for i in range (num,0,-1):
#     fact *= i
# print(fact)

# lists = [1,2,3,4,5,6,7,8,9]
# def length_of_list(list):
#     return len(list)
# print(length_of_list(lists))

# lists = [1,2,3,4,5,6,7,8,9]
# def el_list(list):
#     print(list)
# el_list(lists)

# lists = [1,2,3,4,5,6,7,8,9]
# def el_list(list):
#     for el in list:
#         print(el, end = " ")
# el_list(lists)

# def fact(num):
#     nums = 1
#     for i in range(num,1,-1):
#         nums *= i
#     return nums

# print(fact(5))
 
# dict1 ={
#     "table" : "a piece of furniture",
#     "cat" : "a small animal",
#     "pen" : "a type of stationary",
#     "laptop" : "a type of electronics"
# } 

# print(dict1.get("new"))

# f = open("practice.txt","w")

# f.write("Hi Everyone\nWe are learning file I/O\nUsing Java\nI like programming in Java")

# f.close()

# def repl(file_address):

#     f = open(file_address,"r+")

#     data = f.read()

#     new_data = data.replace("Java","Python")

#     f.seek(0)

#     f.truncate()

#     f.write(new_data)

#     f.close()

# repl("practice.txt")

# f = open("practice.txt","r")

# data = f.read()

# i = data.find("learning")

# if i >= 0:
#     print("word found")
# else:
#     print("Word does not exist in the string")

# with open("practice.txt","r") as f:
#     data = f.read()

# i = data.find("learning")

# if i != -1:
#     print(f"Word found at {i} index")
# else:
#     print("Word not found")


#counting the numbers in the file
with open("practice.txt","r") as f:
    data = f.read()

numbers = data.split(",")

even_num = 0

for n in numbers:
    n = int(n)
    if n%2==0:
        even_num += 1

print(f"The count of even numbers in the string is {even_num}")