import random

again = True

while again:
    print(random.randint(1, 6))
    another_roll = input("Do you want to reroll? (y/n): ")
    if another_roll.lower() == "y":
        continue 
    else:
        break