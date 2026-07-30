import random
import time
#Do random and list for choosing characters, make 2 randoms and 2 variables, replace "Self.helth in the while loop with the random variables"

class Zoner:
    def __init__(self, name, health, damage, weapon, burst, special, super, ultimate):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.burst = burst
        self.special = special
        self.super = super
        self.ultimate = ultimate
    def attack(self, opponent):
            damage = random.randint(1, self.attack)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")  

    def is_alive(self):
        return self.health > 0 
    
    def is_dead(self):
             return self.health <= 0
class Rushdown:
    def __init__(self, name, health, damage, weapon, burst, special, super, ultimate):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.burst = burst
        self.special = special
        self.super = super
        self.ultimate = ultimate
    def attack(self, opponent):
        damage = random.randint(1, self.attack)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")  

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
         return self.health <= 0
class Allrounder:
    def __init__(self, name, health, damage, weapon, burst, special, super, ultimate):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.burst = burst
        self.special = special
        self.super = super
        self.ultimate = ultimate
    def attack(self, opponent):
        damage = random.randint(1, self.attack)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")  

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
         return self.health <= 0
class Grappler:
    def __init__(self, name, health, damage, weapon, burst, special, super, ultimate):
            self.name = name
            self.health = health
            self.damage = damage
            self.weapon = weapon
            self.burst = burst
            self.special = special
            self.super = super
            self.ultimate = ultimate
    def attack(self, opponent):
        damage = random.randint(1, self.attack)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")  

    def is_alive(self):
        return self.health > 0
    def is_dead(self):
         return self.health <= 0

Ralsei = Zoner("Ralsei", 250, 20, "scarf", 10, 50, 70, 250)
Kris = Rushdown("Kris", 400, 15, "Sword", 10, 40, 40, 100)
Susie = Allrounder("Susie", 550, 30, "Axe", 15, 50, 70, 130)
King = Grappler("King", 600, 15, "Fist", 30, 40, 70, 150)

fighters = [Ralsei, Kris, Susie, King]
your_fighter = random.choice(fighters)
enemy_fighter = random.choice(fighters)
while your_fighter.is_alive() and enemy_fighter.is_alive():
    magic = 0
    print("You are playing as" ,your_fighter.name, "and your opponent is playing as" ,enemy_fighter.name)
    print("Magic meter is" , int(magic),)
    abilities = input("What attack would you like to do? " \
    "Bash. Block. Magic. Ultimate. ")
    if abilities == "Magic":
        print("Your magic moves are Special, Super, Burst. ")
        mgc = input("Which magic move do you want to perform? ")
        if mgc == "Special":
            print(your_fighter.special)
            versus = input("It is the opponents turn now. Opponent, what attack would you like to do?" \
                     "Bash. Block. Magic. Ultimate")
        elif mgc  == "Burst":
            print(your_fighter.burst)
            versus = input("It is the opponents turn now. Opponent, what attack would you like to do?" \
                     "Bash. Block. Magic. Ultimate")
        elif mgc == "Super":
            print(your_fighter.super)
            versus = input("It is the opponents turn now. Opponent, what attack would you like to do? " \
                     "Bash. Block. Magic. Ultimate. ")
    elif abilities == "Bash":
        enemy_fighter.health -= your_fighter.damage
        print("You did ", your_fighter.damage, " damage! ", enemy_fighter.health , " You also gained 10 magic meter!")
        magic += 10
        versus = input("It is the opponents turn now. Opponent, what attack would you like to do? " \
                 "Bash. Block. Magic. Ultimate. ")
    elif abilities == "Block":
         print("You only took" , (enemy_fighter.damage/4), " damage because you blocked!" and "You gained 20 magic")
         versus = input("It is the opponents turn now. Opponent, what attack would you like to do? " \
                  "Bash. Block. Magic. Ultimate. ")
    if abilities == "Ultimate" and magic == 100:
         print("You performed the ultimate. You did " , your_fighter.ultimate, " damage " )
         versus = input("It is the opponents turn now. Opponent, what attack would you like to do? " \
         "Bash. Block. Magic. Ultimate. ")
    elif magic != 100:
         print("You do not have enough magic to perform this ability yet")
         print( abilities)

    versus=""    
    if versus == "Magic": 
            print("Your magic moves are Special, Super, Burst. ")
            mgc = input("Which magic move do you want to perform? ")
            if mgc == "Special":
                print(enemy_fighter.special)
                print( abilities)
            elif mgc  == "Burst":
                print(enemy_fighter.burst)
                print( abilities)
            elif mgc == "Super":
                print(enemy_fighter.super)
                print( abilities)
    elif versus == "Bash":
            print("You did " , enemy_fighter.damage, " damage!" and "You also gained 10 magic meter! ")
            print( abilities)
    elif versus == "Block":
             print("You only took " , (enemy_fighter.damage/4), " damage because you blocked! " and "You gained 20 magic")
             print( abilities)
    if versus == "Ultimate" and magic == 100:
             print("You performed the ultimate. You did " , enemy_fighter.ultimate, " damage " )
             print( abilities)
    elif magic != 100:
         print( abilities)
    if your_fighter.is_dead():
          print("You died. You lose! ")
    elif enemy_fighter.is_dead():
          print("Opponent dead. You win! ")






