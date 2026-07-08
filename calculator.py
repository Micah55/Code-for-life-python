print("Welcome to my video game calculator !!!!")
name = input("Please enter your name: ")
print("Hello, " + name + "! Let's do some calculations.")
game_amount = int(input("How many games would you like to buy? "))
print("You want to buy " + str(game_amount) + " games?")
price_per_game = float(input("How much does each game cost? "))
total_cost = game_amount * price_per_game
print("The total cost for your purchase is: $" + str(total_cost))