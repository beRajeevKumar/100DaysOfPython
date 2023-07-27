# print(round(8/3))
# print(round(8/3, 3))
# print(8//3)
# print(type(8//3)) # It returns integer.

# f-string (Its like templete literal in javascript)
# score = 0
# height = 1.8
# isWinnings = True
 
# print(f"Your Score is {score} and its type is {type(score)}") 
age = input("What is your current age? ")
# You have 12410 days, 1768 weeks, and 408 months left.
total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12
left_days = total_days - int(age)*365
left_weeks = total_weeks - int(age)*52
left_months = total_months - int(age)*12
print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")
