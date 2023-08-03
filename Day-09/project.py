print("Welcome to the secret auction program")

bids_data =[]

def get_bids(bidder_name, bidder_value):
    new_bid ={}
    new_bid["name"]= bidder_name
    new_bid["value"]= bidder_value
    bids_data.append(new_bid)  

should_end = False
while not should_end:
    name=input("What is your name?: ")
    value=int(input("What is your bid?: $"))
    get_bids(bidder_name=name, bidder_value=value)

    again = input("Is there any other bidders? Type 'yes' or 'no'.")
    if again == "no":
         should_end = True

for bid in range(len(bids_data)):
    initial_bid=0
    user_bids=[bids_data[bid]["name"],bids_data[bid]["value"]]
if bids_data[bid]["value"] > initial_bid:
    print(f"The winner is {user_bids[0]} with a bid of ${user_bids[1]}.")
else:
    print("No one wins the bid.")






# The winner is Jams with a bid of $123    