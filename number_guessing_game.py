from random import randint
target = randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > target:
            print("Too high!")
        elif guess < target:
            print("Too low!")
        else:
            print("Congratulation! You guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")