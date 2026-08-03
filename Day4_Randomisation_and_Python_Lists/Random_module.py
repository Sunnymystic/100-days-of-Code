import random
random_integer = random.randint(2,7)  # Returns a random integer N such that a <= N <= b.
print(random_integer)

random_number_0_to_1 = random.random()    # Returns the next random floating point number in the range 0.0 <= x <= 1.0
print(random_number_0_to_1)

#random floating point generator

random_number_a_to_b = random.uniform(1,10)   # Returns a random number between a and b (inclusive)
print(random_number_a_to_b)

# Heads or Tails : Coin flip program
random_number_1_to_10 = random.randint(1,10)
if random_number_1_to_10 % 2 == 0:
    print("Heads")
else:
    print("Tails")