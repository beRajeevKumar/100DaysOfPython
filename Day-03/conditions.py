# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))


# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride the rollercoaster")


# //////////////////////////////////////////////////////////////////
    # Exercise 1 - Odd or Even
# number = int(input("Which number do you want to check? "))

# if number%2==0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# //////////////////////////////////////////////////////////////////
# Nested if/else
# bill=0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill=5
#         print("Child tickets are $5.")
#     elif age<=18:
#         bill=7
#         print("Youth tickets are $7.")
#     else:
#         bill=12
#         print("Adult tickets are $12.")

#     want_photo=input("Do you want a photo taken? Y or N. ")   
#     if want_photo=="Y":
#         bill+=3
#     print(f"Your final bill is ${bill}.")

# else:
#     print("Sorry, you have to grow taller before you can ride the rollercoaster")


# Excercise 2 - BMI Calculator 2.0

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi=round(weight/height**2)

# if bmi <=18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi <=25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi <=30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi <=35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# //////////////////////////////////////////////////////////////////
# year = int(input("Which year do you want to check? "))

# if year %4 ==0:
#     if year %100 ==0:
#        if year %400 ==0:
#            print("Leap year.")
#        elif year %400 !=0:
#           print("Not leap year.")
#     elif year %100 !=0:
#        print("Leap year")
# else:
#    print("Not leap year")

# Exercise 4 - Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill=0

if size == "S":
    bill+=15
elif size == "M":
    bill+=20
else:
    bill+=25

if add_pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_cheese == "Y":
    bill+=1  

print(f"Your final bill is: ${bill}.")      