# Name : Ernest Matata
# Date : 22/06/2026
# Program to show user input in Python
# Get user input for name and age
name = input("Please enter your name: ")
age = input("Please enter your age: ")
# Display the user input
print(f"Hello {name}, you are {age} years old.")   
# Display greetings after getting user input
# Greet the user based on their name
print(f"Welcome to the Python programming world, {name}!")
# Display a message based on the user's age
# Convert age to an integer for comparison
age = int(age)
if age < 18:
    print("You are a minor. Enjoy your youth!") 
else:
    print("You are an adult. Enjoy the responsibilities!")  