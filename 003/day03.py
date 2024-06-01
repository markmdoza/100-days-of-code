# If, else statements. Here we go again!
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Rollercoaster example with age
if height >= 120:
    print("You can ride the rollercoaster!")
    # If statement for age here
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    #else if = elif
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
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