# Lesson 5 Homework: Combining Conditions with Logical Operators
## Enhancing Decision-Making in Python

my_title = "________Eligibility for Benefits________"
print(my_title)

# Defining variables to accept input from the user
f_name = input("Name: ")
age = int(input("Enter your age: "))
is_student = bool(input("Are you a student?(Yes/No): "))
is_employed = bool(input("Are you employed?(Yes/No): "))

# Using logical operators to determine and print eligibility messages for different benefits
if is_student and age <= 25:
    print(f"Congragulations {f_name}, you are eligible for a student discount.")
elif is_employed and age >= 18 or age <= 65:
    print(f"Congragulations {f_name}, you are eligible for work benefits.")
elif is_student or is_employed :
    print(f"Congragulations {f_name}, you are eligible for general benefits.")
else:
    print(f"Sorry {f_name}, you are not eligible for general benefits.")



