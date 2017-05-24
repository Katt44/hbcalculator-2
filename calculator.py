"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


print "howdy welcome to our prefex Calculator! \n "
print "please enter the operators first then operands followed by spaces to complete your equation. \n"

# while loop
# user input, 
# store user input
#tokenize input
#take first token store it,   
#determine what operators from first token index  what function to use
#then run funct

while True:
    user_input = raw_input("> ")
    tokenize_user_input = user_input.split(" ")
    first_token = tokenize_user_input[0]
    print first_token


# Your code goes here
