# If, else statements. Here we go again!
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Rollercoaster example with age + photo and bill charging.
if height >= 120:
    print("You can ride the rollercoaster!")
    # If statement for age here
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    #else if = elif
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

wants_photo = input('Do you want your photo taken? Y or N')
    if wants_photo = 'Y':
        # A better syntax for writing bill = bill + 3
        bill += 3

    print(f'You final bill is {bill}')
else:
    print("Sorry, you need to be taller to ride the rollercoaster!")

# Odd or Even Challenge
# Which number do you want to check?
# number = int(input())
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# if number % 2:
#   print("This is an odd number.")
# else:
#   print("This is an even number.")

# Angela's solution
# Which number do you want to check?
# number = int(input())

# If the number can be divided by 2 with 0 remainder.
# if number % 2 == 0:
#   print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
# else:
#   print("This is an odd number.")

# Nested if/else statements:
    # if condition:
        # if another condition:
            # do this
        # else:
            # do this
    #else:
    # do this

# BMI 2.0 Calculator
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2
bmi_as_int = bmi
# print(bmi_as_int)

if bmi_as_int < 18.5:
  print(f'Your BMI is {bmi_as_int}, you are underweight.')
elif bmi_as_int >= 18.5 and bmi_as_int < 25:
  print(f'Your BMI is {bmi_as_int}, you have a normal weight.')
elif bmi_as_int >= 25 and bmi_as_int < 30:
  print(f'Your BMI is {bmi_as_int}, you are slightly overweight.')
elif bmi_as_int >= 30 and bmi_as_int < 35:
  print(f'Your BMI is {bmi_as_int}, you are obese.')
else:
  print(f'You BMI is {bmi_as_int}, you are clincally obese.')

# Leap Year Code Challenge
# My solution
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 and year % 100 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
  print('Leap year')
else:
  print('Not leap year')

# Angela's Solution
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

# Pizza Coding Challenge
# My solution
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if size == 'S':
  bill = 15
elif size == 'M':
  bill = 20
elif size == 'L':
  bill = 25

if add_pepperoni == 'Y' and size == 'S':
  bill += 2
elif add_pepperoni == 'Y' and (size == 'M' or size == 'L'):
  bill += 3

if extra_cheese == 'Y':
  bill += 1

print(f'Your final bill is: ${bill}.')

# Angela's solution
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")