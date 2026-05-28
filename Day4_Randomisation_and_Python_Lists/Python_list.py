import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]
#append() is to add an item into the end of the list.
#extend() is to adding another list to the end of a list.

#random_number_1_to_5 = random.randint(1,5)
#instead of randint which only takes the range we can use choice function which takes a list as an input.
print(random.choice(friends))


# # Nested lists
# ###dirty_dozen = [    "Strawberries",
#     "Spinach",
#     "Kale, Collard, and Mustard Greens",
#     "Grapes",
#     "Peaches",
#     "Pears",
#     "Nectarines",
#     "Apples",
#     "Bell and Hot Peppers",
#     "Cherries",
#     "Blueberries",
#     "Green Beans"]

dirty_fruits = [
    "Strawberries",
    "Grapes",
    "Peaches",
    "Pears",
    "Nectarines",
    "Apples",
    "Cherries",
    "Blueberries"
]

dirty_vegetables = [
    "Spinach",
    "Kale, Collard, and Mustard Greens",
    "Bell and Hot Peppers",
    "Green Beans"
]

dirty_dozen = [dirty_fruits,dirty_vegetables]

print(dirty_dozen)