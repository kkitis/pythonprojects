import random 

holy_number = random.randint(1,100)

while True:
    guess = int(input("Guess the holy number (between 1 and 100): "))
    if guess < holy_number:
        print("Too low! Try again.")
    elif guess > holy_number:
        print("too high! Try again.")
    else:
        print("thats correct ma ma oooooooooooo!")
        break 