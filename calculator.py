"""A prefix-notation calculator.

Using the arithmetic.py file, we created a prefix
calculator program.
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
print "'square' equals 'square' \n"




while True:
    user_input = raw_input("> ")

    tokenize_user_list = user_input.split(" ")

    first_token = tokenize_user_list[0]

    second_token = int(tokenize_user_list[1])

    if len(tokenize_user_list) == 3:
        third_token = int(tokenize_user_list[2])

    if user_input.lower() == "q" or  user_input.lower() == "quit":
        break


    if first_token == "+":
        print add(second_token, third_token)

    elif first_token == "-":
        print subtract(second_token, third_token)

    elif first_token == "*":
        print multiply(second_token, third_token)

    elif first_token == "/":
        print divide(second_token, third_token)

    elif first_token == "square":
        print square(second_token)
 
    elif first_token == "cube":
        print cube(second_token)

    elif first_token == "pow":
        print power(second_token, third_token)

    elif first_token == "mod":
        print mod(second_token, third_token)

    else:
        print "That's invalid."

  



### This Is Our Pseudo Code:

# while loop
# user input, 
# store user input
#tokenize input
#take first token store it,   
# for loop thru token list
# if pow run the function
#determine what operators from first token index  what function to use
#then run funct
# use dictionaries. optipnal
# quit