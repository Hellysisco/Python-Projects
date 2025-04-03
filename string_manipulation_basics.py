# Lesson 6 Homework: String Manipulation Basics

my_title = "_________String Manipulation_________"
#1.Concatenation
## User enters their first name and last name
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
## Combining them into a full name and displaying it
full_name = first_name + " " + last_name
print(f"Your Full Name is {full_name}")

#2. Indexing
## Asking the user to input a word
word = input("Name one of your favorite drink: ")
## Displaying the first and last character of the word
print(f"The first character of your favorite drink is {word[0]}")
print(f"The last character of your favorite drink is {word[-1]}")