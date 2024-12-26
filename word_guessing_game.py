import random
import re

def reads_words():
    try:
        with open("words.txt") as words_file:
            words_array = words_file.read().splitlines()
            return words_array
    except FileNotFoundError:
        print("File not found")
        return []
    
def get_letter():
    while True:
        letter = input("Enter a letter: ").lower()

        if len(letter) != 1:
            print("Enter only one letter")
            continue
        elif not re.search("[a-z]", letter):
            print("Enter only letters from a to z")
            continue

        return letter

def main():
    words_array = reads_words()
    attempts = 6

    if not words_array:
        print("No words loaded.")
        return

    guess = random.choice(words_array)
    guessed_word = "_" * len(guess)

    print(guessed_word)
    while attempts > 0:

        letter = get_letter()

        if letter in guess:
            if letter in guessed_word:
                print("You already guessed that letter.")
                continue

            print("Good guess")

            guessed_word = "".join(c if c in letter or c in guessed_word else "_" for c in guess)

            if guess == guessed_word:
                print("Congratulations! You guessed the word")
                break
        
            print(guessed_word)
        else:
            print("Wrong guess")
            attempts -= 1

    print(f"Game over! The word was {guess}")


if  __name__ == "__main__":
    main()