# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_name=name1.lower()+name2.lower()
count_true=0
count_love=0

count_true += both_name.count('t')
count_true += both_name.count('r')
count_true += both_name.count('u')
count_true += both_name.count('e')

count_love += both_name.count('l')
count_love += both_name.count('o')
count_love += both_name.count('v')
count_love += both_name.count('e')
score = str(count_true) + str(count_love)
love_score = int(score)

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
