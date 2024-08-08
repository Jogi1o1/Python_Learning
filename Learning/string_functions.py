# String functions
var = "heLLo woRLd"
print(var)

# len(string) function is used to calculate the length of the string
print(len(var))

# str(value) function is used to change value of any other datatype to string
number = 123
name = str(123)
print(type(name))

# string.upper() function is used to change all the characters of the string to uppercase
print(var.upper())

# string.lower() function is used to change all the characters in the string to lowercase
print(var.lower())

# string.captalize() makes first letter of string capital
print(var.capitalize())

# string.title() makes the first letter of every word in string capital
print(var.title())

# string.strip() removes the leading and trailing spaces of the string
var_1 = "   heLLo woRLd  "
print(var_1.strip())

# string.rstrip() removes the trailing spaces of the string
var_1 = "   heLLo woRLd  "
print(var_1.rstrip())

# string.lstrip() removes the leading spaces of the string
var_1 = "   heLLo woRLd  "
print(var_1.lstrip())

# string.find("value") finds the index of the first occurence of the value in the string
print(var.find('L'))

# string.rfind("value") finds the index of the last occurence of the value in the string
print(var.rfind('L'))

# string.index("value") finds the index of first occurence of value in the string and raises 'ValueError' if the value is not found in the string
print(var.index('L'))

# string.rindex("value") fing the index of last occurence of the value in the string and raises 'ValueErro' if the value is not present in the string
print(var.rindex('L'))

# string.startswith("value") checks if the given string starts with the value or not
print(var.startswith('he'))

# string.endswith("value") checks if the given string ends with the given value or not
print(var.endswith('Ld'))

# string.isalpha() checks if the string contains only alphabet or not
print(var.isalpha())

# string.isdigit() checks if the string contains only digit or not
var_2 = "98765"
print(var_2.isdigit())

# string.isalnum() checks if the string contains alphabet and numeric value or not
var_3 = "abcd@1234"
print(var_3.isalnum())

# string.split() splits a string into a list using a delimeter
var_4 = "hello,world"
print(var_4.split(','))

# string.splitlines() splits a string into a list at line breaks
var_5 = "hello\nworld"
print(var_5.splitlines())

# " ".join(list) will add whole list into a single string
list_1 = ["hello","world"]
print(" ".join(list_1))

# string.replace("value_1","value_2") method will replace value_1 in the string to value_2
print(var.replace("woRLd","thERe"))


