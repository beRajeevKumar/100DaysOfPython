travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
# new_values = {
#     "country": "Russia",
#     "visits": 2,
#     "cities": ["Moscow", "Saint Petersburg"]
#   }
# travel_log.append(new_values)

# print(travel_log)
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(visit_country, total_visites, cities_visit):
    add_country = {
        "country": visit_country,
        "visits": total_visites,
        "cities": cities_visit 
    } 
    travel_log.append(add_country)
    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)