#recursion

# recursive function to calculate the factorial of any given number
# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(3))

#recursive function to calculate the sum of n natural numbers 
# def natural_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + natural_sum(n-1)
    
# print(natural_sum(10))

#recursive function to print all the items in the list
def el(list,n=0):
    if n < len(list):
        print(list[n])
        el(list,n+1)

lists = [1,3,5,7,9]

el(lists)

# def rtraverse(seq, i=0):
#     if i < len(seq):
#         print(seq[i])
#         rtraverse(seq, i+1)

# rtraverse(lists)

