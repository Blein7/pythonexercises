import random
import os


def guess_number(user_input, computer_guess):
    if user_input < computer_guess:
        return "Too low"
    elif user_input > computer_guess:
        return "Too high"
    elif user_input == computer_guess:
        return "You guessed the number correctly!!!"


def play():

    computer_guess = random.randint(1, 100)
    should_continue = False
    print(f"I'm thinking of a number between 1 and 100.\n Pssst, the correct answer is {computer_guess} ")
    lives = input("Choose a difficulty. Type 'easy' or 'hard':")
    if lives == 'easy':
        number_of_tries = 10
    elif lives == "hard":
        number_of_tries = 5
    user_input = int(input("Enter your guess:"))
    while not should_continue:
        print(guess_number(user_input, computer_guess))
        if user_input == computer_guess:
            should_continue = True
        else:
            number_of_tries -= 1
            print(f"You have {number_of_tries} attempts remaining to guess the number")
            user_input = int(input("Guess again:"))
        if number_of_tries == 1:
            should_continue = True
            print("You have used up all your attempts")


while input("Do you want to play, yes/no:") == 'yes':
    os.system('cls')
    play()
