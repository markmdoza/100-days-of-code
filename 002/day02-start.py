# Data Types
# String
# print("Hello"[4]) # This is called subscripting.

# Integer
# print(123 + 345)
# 123_456_789

# Float
# 3.14159

# Boolean
# True
# False

# num_char = len(input("What is your name? "))
# # Type conversion (turning a integer into a string).
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# Type checking
# Use type function to check what type of data type you're working with.
# You can then use str, int, or float to change the data types.
# print(type(num_char))
# a = str(123)
# print(type(a))

# Data types coding challenge
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
# My solution
num1 = two_digit_number[0]
num2 = two_digit_number[1]

print(int(num1) + int(num2))

# Angela's solution
# two_digit_number = input()
#
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
#
# # Add the two integers together
# two_digit_number = first_digit + second_digit
#
# print(two_digit_number)

# BMI Challenge - Angel's solution
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

# My solution

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

h = float(height)
w = float(weight)

h_int = int(h)
w_int = int(w)

print(round(w / (h * h)))

# Number manipulation and f strings
# print(round(8 / 3, 2) - rounds numbers up or down. Adding the comma and a number rounds it the decimal
# of the number placed.
# print(8 // 3) - creates an int without even adding the int function.

# result = 4 / 2 - you can continue arethmetic to this 'result variable'
# result /= 2
# print(result) - will return 1.

# score = 0
# height = 1.8
# isWinning = True
#f-string
# f'Your score is {score}'

# You can use
# +=
# -+
# to increase or decrease the value.

# Life In Weeks Challenge

# MY SOLUTION
# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# new_age = int(age)
# alive_until = 90
# weeks_in_a_year = 52
#
# years_left = alive_until - new_age
#
# num_of_weeks = years_left * weeks_in_a_year
# print(f"You have {num_of_weeks} weeks left.")

# ANGELA'S SOLUTION
# age = input()
# Your code below this line 👇
# years = 90 - int(age)
# weeks = years * 52
#
# print(f"You have {weeks} weeks left.")

