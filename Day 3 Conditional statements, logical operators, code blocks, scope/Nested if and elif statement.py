bill = 0
height = int(input("What is your height ?"))
if height > 120:
    print("You are allowed on the ride")
    age = int(input("What is your age ?"))
    if(age <= 18 and age >=12):
        bill = 7
        print("You should pay $7")
    elif(age < 12):
        bill = 5
        print("You should pay $5")
    elif(45 <= age <= 55):
        print("Everything is going to be OK, Have a free ride on us!")
    else:
        bill = 12
        print("You should pay $12")
    wants_photo = input("Do you want to click a photo ? Type 'Y' for Yes and 'N' for No")
    if wants_photo == "y":    # Add $3 to the bill
        bill += 3
    print(f"You final bill is {bill}")
else:
    print("You are not allowed on the ride")
