# Name : Ernest Matata
# Date : 22/06/2026
# Program to demonstrate string formatting in Python
Name = "Ernest Matata"
Age = 18
print(f"My name is {Name} and I am {Age} years old.")

# Get String Length
from io import open_code

sentence = "Python is a powerful programming language."
string_length = len(sentence)
print(f"The length of the sentence is: {string_length} characters.")

# Splitting a String
sentence = "Python is a powerful programming language." 
words = sentence.split()
print(f"The words in the sentence are: {words}")

# Making everything uppercase
mpesa_code = "uekbs4vbl8"
capitalized = mpesa_code.upper()
print(f"The capitalized MPESA code is: {capitalized}")

# Making everything lowercase
mpesa_code = "UEKBS4VBL8"
lowercase = mpesa_code.lower()
print(f"The lowercase MPESA code is: {lowercase}")

# Replacing characters in a string
balance = "Ksh 100"
amount_added = "Ksh 500"

cleaned_balance = balance.replace("Ksh ", "")

print(f"Cleaned balance: {cleaned_balance}")

cleaned_amount = amount_added.replace("Ksh ", "")

print(f"Cleaned amount added: {cleaned_amount}")

total_balance = int(cleaned_balance) + int(cleaned_amount)
print(f"Total balance after adding amount: Ksh {total_balance}")
print(f"You have received Ksh {cleaned_amount} from Kilian and your new balance is Ksh {total_balance}.")