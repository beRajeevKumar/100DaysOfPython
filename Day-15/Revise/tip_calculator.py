print("Welcome to the tip calculator🙏🏻")
total_bill = float(input("What was total bill? $"))
people = float(input("How many people to split the bill? "))
tip_percentage = float(
    input("What percentage would you like to give? 10, 12, 15? "))

bill_per_person = round(
    (total_bill + (total_bill*tip_percentage)/100)/people, 2)

print(f"Each person should pay: {bill_per_person}")
