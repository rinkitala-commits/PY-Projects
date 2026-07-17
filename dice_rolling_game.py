import random

def roll_the_dice():
    while True:
        choice = input("Roll the Dice? (yes / no): ") .lower()
        if choice == "y" or choice == "yes" :
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            # print(f"({die1}, {die2})")
            print(f"(You rolled a {die1} and a {die2})")

        elif choice == "n" or choice == "no" :
            print("Thank You for Playing!")
            break
        
        else:
            print("Invaid Choice!")


roll_the_dice()