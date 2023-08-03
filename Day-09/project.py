from art import logo
print(logo)

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

highest_bid=0
winner=""
for bid in range(len(bids_data)):
    if bids_data[bid]["value"] > highest_bid:
        highest_bid = bids_data[bid]["value"]
        winner=bids_data[bid]["name"]
print(f"The winner is {winner} with a bid of ${highest_bid}.")
