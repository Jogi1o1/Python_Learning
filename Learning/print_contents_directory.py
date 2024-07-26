import os
# os module is used to import the methods that can be performed on the operating system
arr = os.listdir('.')
# Using listdir() method to get all the contents from the specified directory and storing in an array
print(arr)
# Printing arr -  an array that store the data of the files stored in the directory