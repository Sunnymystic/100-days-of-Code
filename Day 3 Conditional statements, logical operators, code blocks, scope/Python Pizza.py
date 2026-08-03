#Small Pizza (S): $15
#Medium Pizza (M): $20
#Large Pizza (L) : $25
#Add Pepperoni to small pizza: +$2
#Add Pepperoni to medium or large pizza: +$3
#Add extra chesse for any size pizza: $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
extra_chesse = input("Do you want extra chesse? Y or N: ")
Total_prize = 0
if size in ("S", "M", "L"):
    if size == "S":
        Total_prize += 15
    elif size == "M":
        Total_prize += 20
    else:
        Total_prize += 25

    if pepperoni == "Y":
        if size == "S":
            Total_prize += 2
        else:
            Total_prize += 3

    if extra_chesse == "Y":
        Total_prize += 1

    print("Your Total_prize  = " + str(Total_prize))
else:
    print("Invalid size. Please enter S, M, or L.")
    




