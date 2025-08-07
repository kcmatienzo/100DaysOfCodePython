print("Welcome to the Python Pizza deliveries!")
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0


if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
else:
    print("You typed the wrong inputs.")

print(f"Your final bill is ${bill}")