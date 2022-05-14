import random

value = random.randint(1, 99)
trials = 0

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
guess = input("What's your guess between 1 and 99?\n>> ")
while guess != "exit":
    trials += 1
    if not guess.isdigit():
        print("That's not a number.")
    elif int(guess) < value:
        print("Too low!")
    elif int(guess) > value:
        print("Too high!")
    else:
        if value == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        else:
            print("Congratulations, you've got it!")
        if trials == 1:
            print("You got it on your first try")
        else:
            print("You won in  {} attempts".format(trials))
        break
    guess = input("What's your guess between 1 and 99?\n>> ")
print("Goodbye!")
