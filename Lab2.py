# randrange(0,6) includes first parameter but not second parameter aka includes 0 but not 6
# randint(0,6) includes both parameters
#for loop_variable in range(10):
 #   print(loop_variable)

#for count in range(10):
#    print(count)

# PSYCHIC GUESSING GAME #
print("It's time for your psychic power evaluation!")
correct_guesses = 0
for count in range(12):
    user_number = input("Pick a number from 1 to 6. ")
    from random import(randrange)
    generated_number = str(randrange(1,7))
    print("You guessed", user_number + ", but the correct number was " + generated_number + ".")
    if int(user_number) == int(generated_number):
        correct_guesses = correct_guesses + 1
print("You guessed correctly", correct_guesses, "times.")
if correct_guesses < 4:
    print("You may not be a psychic.")
else:
    print("You may be a psychic.")