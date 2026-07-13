import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Dice Rolling Simulator")
while roll_dice() != 6:
     print(roll_dice())
     if roll_dice() == 6:
        print("You rolled a 6! You win!")
        break
main()
