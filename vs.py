import random
import time

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

Ralsei = Zoner("Ralsei", 250, 20, "scarf", 10, 50, 70 "Heal prayer")
Kris = Rushdown("Kris", 400, 15, "Sword", 10, 40, "Heal" 100)
Susie = Allrounder("Susie", "550", "30", "Axe", "Roar", "Rude buster", "Throw", "Red buster")
King = Grappler("King", "600", "15", "Fist", "Dual spades", "Choke", "Spade barrage", "Card slam")





