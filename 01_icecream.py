# Icecream list
icecream = ["Chocolate", "Mint Chocolate Chip", "Hokey Pokey","French Vanilla"]

# Ask user for fav icecream
favourite = input("Whats your favourite ice cream flavour?")

# If in list provide feedback
if favourite in icecream:
    print("Well done, it's on the list")
else:
    print("Sorry thats not on the list")

# Print list items and item length
for item in icecream:
    print(list(item),len(item))