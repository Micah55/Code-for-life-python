print(" <<<Welcome to Madlibs! Please enter the following words to complete the story.!!!>>>  :)")

print("I saw a girl and I thought she was _________")
adjective1 = input("Please enter an adjective: ")
if adjective1 != "Beautiful" and adjective1 != "beautiful" and adjective1 != "Pretty" and adjective1 != "pretty" and adjective1 != "Attractive" and adjective1 !="attractive" and adjective1 != "Ugly" and adjective1 != "ugly":
    raise TypeError("You didn't enter the correct adjective. Your hint is a word that means 'attractive'.")
    adjective1 = input("Please enter an adjective: ")
elif adjective1 == "Beautiful" or adjective1 == "beautiful" or adjective1 == "Pretty" or adjective1 == "pretty":
    print(f"I saw a girl and I thought she was {adjective1}")
    print("I went to talk to her but she was _________" + " and wanted to sleep")
elif adjective1 == "Ugly" or adjective1 == "ugly":
    print("I saw a girl and thought she was ugly so I didnt't talk to her")
adjective2 = input("Please enter an adjective: ")
if adjective2 != "Tired" and adjective2 != "tired" and adjective2 != "Sleepy" and adjective2 != "sleepy" and adjective2 != "Exhausted" and adjective2 != "exhausted":
    raise TypeError("You didn't enter the correct adjective. Your hint is a word that means 'exhausted'.")      
    adjective2 = input("Please enter an adjective: ")
elif adjective2 == "Tired" or adjective2 == "tired" or adjective2 == "Sleepy" or adjective2 == "sleepy":
    print(f"I went to talk to her but she was {adjective2} and wanted to sleep")
elif adjective2 == "Exhausted" and adjective2 == "exhausted":
    print("Did you really think that was the answer dummy. Try again.")
else:
    raise TypeError("You didn't enter an adjective. Please try again.")
    adjective2 = input("Please enter an adjective: ")
print("I was suprised because she looked _________"+ " but looks can be decieving")
adjective3 = input("Please enter an adjective: ")
if adjective3 != "Energetic" and adjective3 != "energetic" and adjective3 != "Lively" and adjective3 != "lively":
    raise TypeError("You didn't enter the correct adjective. Your hint is a word that means 'energetic'.")
    adjective3 = input("Please enter an adjective: ")
elif adjective3 == "Energetic" or adjective3 == "energetic" or adjective3 == "Lively" or adjective3 == "lively":
    print(f" I was suprised because she looked {adjective3} but looks can be decieving")
else:
    raise TypeError("You didn't enter an adjective. Please try again.")
    adjective3 = input("Please enter an adjective: ")
print("I said bye and went home and realized I was _________" + " too")
adjective4 = input("Please enter an adjective: ")
if adjective4 != "Tired" and adjective4 != "tired" and adjective4 != "Sleepy" and adjective4 != "sleepy":
    raise TypeError("You didn't enter the correct adjective. Your hint is a word that means 'exhausted'.")
    adjective4 = input("Please enter an adjective: ")
elif adjective4 == "Tired" or adjective4 == "tired" or adjective4 == "Sleepy" or adjective4 == "sleepy":
    print(f"I said bye and went home and realized I was {adjective4} too")
else:
    raise TypeError("You didn't enter an adjective. Please try again.")
    adjective4 = input("Please enter an adjective: ")
print("when I woke up, I was _________" + " but I was still _________" + " enough to go and look for her")
adjective5 = input("Please enter an adjective: ")
adjective6 = input("Please enter an adjective: ")
if adjective5 != "Sad" and adjective5 != "sad" and adjective6 != "Happy" and adjective6 != "happy":
    raise TypeError("You didn't enter the correct adjective. Your hint is a word that means 'depressed' and for the second one, it's a word that means 'the opposite of sad'.")
    adjective5 = input("Please enter an adjective: ")
    adjective6 = input("Please enter an adjective: ")
elif adjective5 == "Sad" or adjective5 == "sad" or adjective6 == "Happy" or adjective6 == "happy":
    print(f"when I woke up, I was {adjective5} but I was still {adjective6} enough to go and look for her")

#elif adjective1 == "attractive":
    #print("You dirty little cheater, did you relly think I would give you the answer")
    #adjective1 = input("Please enter an adjective: ")
#if adjective1 == "Ugly" or adjective1 == "ugly":
    #print("I saw a girl and thought she was ugly so I didnt't talk to her")
    #print("I was no longer _________ that day so I went back home")
    #adjectivepart2 = input("Please enter a adjective: ")
    #if adjectivepart2 != "Excited" or adjectivepart2 != "excited":
        #raise TypeError("Incorrect adjective. Your hint is that the adjective is is similar to 'enthusiastic' or 'happy'")
    #elif adjectivepart2 == "Excited" or adjectivepart2 == "excited":
        #print(f"I was no longer {adjectivepart2} so I went back home.")
        #print("I took a shower and realized that I was _________ and that I would never get a girl so I went to sleep in tears")
        #adjectivepart3 = input("Please enter an adjective: ")
        #if adjectivepart3 != "Hopeless" or adjectivepart3 != "hopeless":
            #raise TypeError("Incorrect adjective. Your hint is, the word means 'to not have any hope' ")
        #elif adjectivepart3 == "Hopeless" or adjectivepart3 == "hopeless":
            #print(f"I took a shower and realized the I was {adjectivepart3} and that I would never get a girl so I went to sleep in tears.")
else:
  raise TypeError("You didn't enter an adjective. Please try again.")
  adjective1 = input("Please enter an adjective: ")


