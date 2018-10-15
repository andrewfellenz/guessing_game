# Start of file
from random import randint

# Variables for all the lines of code needed

number_to_guess = randint(1, 100)

guess_number = 1

score_board = []

high_score = False

# Functions to pick a random int and display scoreboard

def player_guess(guess_number):
    while True:
        try:
            guess = int(input("Guess #{}> ".format(guess_number)))
        except ValueError:
            print("That's not a number")
        else:
            if guess < 1 or guess > 100:
                print("You can only guess numbers between 1 and 100.")
                continue
            else:
                return guess
                break

print("Welcome to Drew's Guessing Game. The object of the game is to guess the correct number in the fewest guesses possible. Good luck!\n")


def play_game()
  while True:
      guess = player_guess(guess_number)
      if guess == number_to_guess:
          if guess_number < high_score or high_score == False:
              print("{} is the correct number! Your score of {} guesses is the new high score!".format(guess, guess_number))
              high_score = guess_number
              break
          else:
              print("{} is the correct number and you guessed it in {} guesses!".format(guess, guess_number))
              
              break
      elif guess > number_to_guess:
          print("That number is too high.")
          guess_number += 1
      elif guess < number_to_guess:
          print("That number is too low.")
          guess_number += 1

play_game()




 
# end game and display guesses

# Ask user if they would like to play again
