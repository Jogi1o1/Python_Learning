# file_io

# # to open a file we use open() function.
# f = open("helloguys.txt","r")

# to read whole data of the file
# data = f.read()

# # to read the sentence of the file and store its data in a variable
# data = f.readline()

# # to close the file we can use close function
# f.close()

# print(data)

# # to replace the old data with new data
# f= open("helloguys.txt","w")

# # adding new data to the file
# f.write("This is a new beggining")

# # closing the file
# f.close()

# # to add new data at the end of old data in the file
# f = open("helloguys.txt","a")

# # adding new data to the file
# f.write("\nEnjoy the day")

# # closing the file
# f.close()

# # to read and overwrite data in the file where the pointer is at the start of the file and file is not truncated
# f = open("helloguys.txt","r+")

# # replacing data from the start of the file
# f.write("that")

# #closing the file
# f.close()

# # to read the file and overwrite data in the file where the pointer is at the start of the file and file is truncated before starting read operation
# f = open("helloguys.txt","w+")

# # removing old data and entering new data in the file
# f.write("Hello")

# # closing the file
# f.close()

# # to read and append data in the file where the pointer is at the end of the data in the file and file is not truncated
# f = open("helloguys.txt","a+")

# # appending new data at the end of the old data in the file
# f.write("\nwassup")

# # closing the file
# f.close()

# #deleting the file
# import os

# # removing the file from the system
# os.remove("helloguys.txt")

