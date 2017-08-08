
import random

keep_playing = "Yes"

while keep_playing.strip().lower() == "yes":


    user_input = raw_input("What is your question")


    fortunes = ["You will lose all your hair", "You will marry a beauty", "You will live till your 85", "You will live in Thailand for a year", "You will have chinese food for lunch", "You will visit Europe next year", "You will be rich in 5 years"]



    print (random.choice(fortunes))

    keep_playing = raw_input("Would you like to continue playing?")
