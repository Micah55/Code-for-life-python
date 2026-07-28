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
        return self.health 
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
        return self.health 
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
        return self.health 
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
        return self.health 

Ralsei = Zoner("Ralsei", 250, 20, "scarf", 10, 50, 70, 250)
Kris = Rushdown("Kris", 400, 15, "Sword", 10, 40, 40, 100)
Susie = Allrounder("Susie", 550, 30, "Axe", 15, 50, 70, 130)
King = Grappler("King", 600, 15, "Fist", 30, 40, 70, 150)

while self.health > 0:
     print("Magic meter is" int(magic))
     abilities = input("What attack would you like to do?" \
     "Bash. Block. Magic. Ultimate")
     if abilities == "magic":
        print("Your magic moves are Special, Super, Burst, ")
        mgc = input("Which magic move do you want to perform?")
        if mgc == "Special":
            print(self.special)
        elif mgc  == "Burst":
            print(self.burst)
        elif mgc == "Super":
            print(self.super)
     elif abilities == "Bash":
        print("You did" self.damage "damage!" and "You also gained 10 magic meter!")
     elif abilities == "Block":
         print("You only took" int(opponent_damage/4) "because you blocked!" and "You gained 20 magic")
     elif abilities == "Ultimate":
         print("You performed the ultimate. You did" self.ultimate "damage" )


        







