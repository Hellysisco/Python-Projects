#Lesson 4 Homework: Control Flow with Conditionals
##Making Decisions in Your Python Programs
my_title = "--------Age Group Indentifier--------"
print(my_title)

# Asking the user for their age
f_name = input("Name: ")
age = int(input("Enter your age: "))

# Using conditional statements to determine the age group
if age < 13:
    print(f"You are a child {f_name}.")
elif 13 >= age <= 19:
    print(f"You are a teenager {f_name}.")
else:
    print(f"You are an adult {f_name}.")

