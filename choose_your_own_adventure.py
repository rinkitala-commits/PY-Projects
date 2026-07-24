name = input("Enter your name: ")
print(f"Hello, {name}! Let's start your adventure.")
answer = input("You find yourself at a dirt road. Do you want to go left or right? (left/right): ").strip().lower()

if answer == "left":
    answer = input("You come to a bridge. Do you want to cross it or go back? (cross/back): ").strip().lower()
    if answer == "cross":
        answer = input("You crossed the bridge and met a friendly traveler.Do you want to talk to them or ignore them? (talk/ignore): ").strip().lower()
        if answer == "talk":
            print("The traveler gives you a treasure map! You win!")
        elif answer == "ignore":
            print("You ignored the traveler and got lost in the forest. Game over.")
    elif answer == "back":
        print("You went back and got lost in the forest. Game over.")
    else:
        print("Invalid choice. You are lost.")

elif answer == "right":
    answer = input("You encounter a wild animal! Do you want to fight it or run away? (fight/run): ").strip().lower()
    if answer == "fight":
        answer = input("You fought the animal and won! You continue your journey. Then you came accross a river. Do you want to swim across or build a raft? (swim/build): ").strip().lower()
        if answer == "swim":
            print("You swam across the river and found a hidden treasure! You win!")
        elif answer == "build":
            print("You built a raft and crossed the river safely. You continue your journey and find a village. You are safe! You win!")
        else:
            print("Invalid choice. You are lost.")
    elif answer == "run":
        print("You ran away and got lost in the forest. Game over.")
    else:
        print("Invalid choice. You are lost.")
else:
    print("Invalid choice. You are lost.")