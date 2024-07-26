# str.title() function

def format_name(f_name,l_name):

    str = f_name.title() + " " + l_name.title()
    return str

first_name = input("What is your fist name?\n")
last_name = input("What is your last name?\n")

formatted_name = format_name(first_name,last_name)
print(f"Your name in camel casing format is {formatted_name}")
    