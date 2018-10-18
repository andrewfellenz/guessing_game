from random import randint

def player_guess(guess_number):
    while True:
        try:
            guess = int(input("Guess #{}> ".format(guess_number)))
        except ValueError:
            print("That's not a number.")
        else:
            if guess < 1 or guess > 100:
                print("You can only guess numbers between 1 and 100.")
                continue
            else:
                return guess
                break

def game_start():

    high_score = False
    
    def play_game(high_score):

        number_to_guess = randint(1, 100)
        guess_number = 1
        if high_score:
            print("\nThe current high score is {}. See if you can beat that. Guess a number between 1 and 100.".format(high_score))
        else:
            print("\nWelcome to Drew's Number Guessing Game.\nType a number between 1 and 100 to guess.\nThe fewer guesses the higher you score!\n")
        while True:
            guess = player_guess(guess_number)
            if guess == number_to_guess:
                if guess_number < high_score or high_score == False:
                    print("\n{} is the correct number!\nThat's the best you've done!\n{} is your new high score!".format(guess, guess_number))
                    high_score = guess_number
                    break
                else:
                    print("{} is the correct number.\n You got it in {} guesses!".format(guess, guess_number))       
                    break
            elif guess > number_to_guess:
                print("That number is too high.")
                guess_number += 1
            elif guess < number_to_guess:
                print("That number is too low.")
                guess_number += 1
      
        while True:
            try:
                new_game = input("\nWould you like to play again? (Yes/No) ")
                new_game = new_game.lower()
                if new_game == "yes":
                    play_game(high_score)
                elif new_game == "no":
                    print("\nThank you for playing.\n")
                    raise SystemExit
                else:
                    raise ValueError("Please enter \"Yes\" or \"No\".")                    
            except ValueError as err:
                print("{}".format(err))
    play_game(high_score)
game_start()
