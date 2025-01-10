import random

def guess_the_number():
    # Step 1: Ask the user for the difficulty setting
    print("Welcome to the Guess the Number game!")
    difficulty = input("Choose difficulty: Easy, Medium, or Hard: ").strip().lower()

    # Step 2: Set the range based on difficulty
    if difficulty == "easy":
        number_range = 10
        max_guesses = 3
    elif difficulty == "medium":
        number_range = 20
        max_guesses = 4
    elif difficulty == "hard":
        number_range = 50
        max_guesses = 5
    

    # Step 3: Generate a random number based on the selected difficulty
    random_number = random.randint(1, number_range)

    # Step 4: Start the guessing game
    print(f"Guess a number between 1 and {number_range}. You have {max_guesses} attempts.")

    attempts = 0
    while attempts < max_guesses:
        user_guess = int(input(f"Attempt {attempts + 1}: Your guess: "))
        attempts += 1

        # Step 5: Check if the guess is correct
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif user_guess < random_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")

        # Step 6: Check if the player has used all attempts
        if attempts == max_guesses:
            print(f"Sorry, you've used all your attempts. The correct number was {random_number}. Better luck next time!")
            break

# Call the function to run the game
guess_the_number()
