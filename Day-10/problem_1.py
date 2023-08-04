# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year.")
#       else:
#         print("Not leap year.")
#     else:
#       print("Leap year.")
#   else:
#     print("Not leap year.")

# def is_leap_year(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# optimise code of is_leap function:
def is_leap(year):
  """"is_leap" function decides whether the year is leap or not with optimised code."""  
  # This is docString which appeares when we call the function and hover the a kind of popup is a docstring. 
  if year%4==0 and year%400==0 or year%100!=0:
    return True
  return False
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




        # String leapYear=(year%4==0 && year%400==0 || year%100!=0)?"Leap year":"Not a Leap year";