print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
tip_per_person = total_bill * (tip_percent/100)
print(f"Tip per person: ${round(tip_per_person/no_of_people, 2)}")
total_per_person = round((total_bill + tip_per_person)/no_of_people, 2)
print(f"Each person should pay: ${total_per_person}")
