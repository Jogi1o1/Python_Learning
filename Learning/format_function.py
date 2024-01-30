# Format function is used to print the number upto desired decimal as in python if we round up any number than the 0's after decimal gets ignored 
# Here we will use round function to round off the variable value
print(round(12.30000000,2))
# Here we will use format function to round off the variable value
fun = "{:.2f}".format(12.30000000)
print(fun)