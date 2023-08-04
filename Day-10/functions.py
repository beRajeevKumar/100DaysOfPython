# def formate_name(f_name,l_name):
#     # full_name = f_name[0].upper()+
#     full_name = f_name+" "+ l_name
#     return full_name.title()

# def formate_name(f_name,l_name):
#     full_name = f_name[0].upper()+f_name[1:] +" "+  l_name[0].upper()+l_name[1:]
#     return full_name.title()

# def formate_name(f_name,l_name):
#     full_name = f_name+" "+ l_name
#     return full_name.capitalize()

# print(formate_name("rajeev","kumar"))

# Myltiple return statements in a function.
def formate_name(f_name,l_name):
    if f_name =="" or l_name == "":
        return "You didn't provide the valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(formate_name(input("What is your first name?"), input("What is your last name?")))