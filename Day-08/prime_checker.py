import math
#Write your code below this line 👇
# def prime_checker(number):
#     count=0
#     if number == 2 and number == 3:
#         print("It's a prime number.")
#     elif number % 2 == 0 and number % 3 == 0:
#         print("It's not prime number.'")
#     for i in range(5, int(math.sqrt(number)),i):
#         if number%i==0 or n%(i+2)==0 :
#             count+=1
#     if count == 0:
#       print("It's a prime number.")
#     else:
#       print("It's not a prime number.")            


def prime_checker(number):
    count = 0
    if number ==1:
        print("It's not a prime number.")           
    for i in range(2, number):
        if number %i ==0:
               count+=1
    if count == 0:
         print("It's a prime number.")
    else:
         print("It's not a prime number.")           
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
