"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


print "howdy welcome to our prefex Calculator! \n "
print "please enter the operators first then operands followed by spaces to complete your equation. \n"
print "instructions: \n   "
print "'addition' equals '+' "
print "'subtraction' equals '-' "
print "'multiplication equals '*' "
print "'division' equals '/' "
print "'power' equals 'pow' "
print "'cube' equals 'cube' "
print "'modulo' equals 'mod' "
print "'square' equals 'square' "


# while loop
# user input, 
# store user input
#tokenize input
#take first token store it,   
# for loop thru token list
# if pow run the function
#determine what operators from first token index  what function to use
#then run funct
# quit

while True:
    user_input = raw_input("> ")
    tokenize_user_input = user_input.split(" ")
    first_token = tokenize_user_input[0]
    second_token = int(tokenize_user_input[1])
    third_token = int(tokenize_user_input[2])


    if first_token == "+":
        total_sum = add(second_token, third_token)
        print total_sum
     


    if user_input.lower() == "q" or  user_input.lower() == "quit":
        break

# Your code goes here
