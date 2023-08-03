# Nesting a list in a dictionary

travel_log ={
  "France":["Paris", "Lille","Dijon"],
  "Germeny":["Berlin","Hamburg","Stuttgart"] 
}
# To Access any element of a nested dictionary in list.
print(travel_log["France"][2])

# Nesting a dictionary in a dictionary
travel_log ={ 
    "France": {"cities_visited":["Paris", "Lille","Dijon"], "total_visits":len(["Paris", "Lille","Dijon"])},
    "India":{"cities_visited":["Delhi", "Bengluru","Indore","Gurugram"], "total_visits":len(["Delhi", "Bengluru","Indore","Gurugram"])}
}

# Nesting a dictionary in a list
travel_log ={ 
    {"Country":"France",
    "cities_visited":["Paris", "Lille","Dijon"],
    "total_visits":2,
    },
    {"Country":"India",
    "cities_visited":["Delhi", "Bengluru","Indore","Gurugram"],
    "total_visits":4
    }
}
