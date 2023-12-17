import random

def guessing_game():
    print("Welcome to the Guessing Game!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0

    while True:
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
