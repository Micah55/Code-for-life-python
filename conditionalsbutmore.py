fighter = "warrior"
key = True
energy = 35

if fighter == "warrior" and key == True:
   print("Congrats you are allowed to open the door.")
   if energy > 30:
      print("You can open the door, energy is sufficient.")
   elif energy < 30:
      print("You can't open the door, energy is too low")
else: 
   print("Come back later")
    