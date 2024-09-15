import random
count: int = 0

while True:
    user_input: str = input("Roll the dice? (y/n): ").lower()

    if user_input == 'y':
        output: list = []
        dice_count: int = int(input("How many dice you want to roll?: "))

        for _ in range(dice_count):
            output.append(random.randint(1, 6))

        print(tuple(output))
        count = count + 1
    elif user_input == 'n':
        print("Thank you for playing")
        print(f"You rolled {count} times in the last session.")
        break
    else:
        print("Invalid input!")