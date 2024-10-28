from random import randint

random_num = randint(1, 10)

while True:
    guess = input("Guess the number from one to ten.")
    guess = int(guess)
    if guess > random_num:
        print("Too high try again.")

    elif guess < random_num:
        print("Too low try again.")

    else:
        print("Congratulations! You've guessed the number.")
        break