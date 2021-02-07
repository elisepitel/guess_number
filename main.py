import random
from replit import clear

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print("Welcome to a Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Function to set difficulty:
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level.lower() == "hard":
    return HARD_LEVEL_ATTEMPTS
  else: 
    return EASY_LEVEL_ATTEMPTS

#Function to compare number to guess with guessed number: 
def guess_number(user_guess, number, turns):
  """Checks answer against guess, Returns the number of turns remaining"""
  if user_guess > number: 
    print("  Too high")
    return turns - 1
  elif user_guess < number: 
    print("  Too low")
    return turns - 1
  elif user_guess == number:
    print(f"  Win! The number to guess was {number} ")


def play():
  #Generate randomly number to guess between 1 and 100: 
  number = random.randint(1, 100)

  #Uncomment following line to test code:
  #print(f"Number to guess is {number}.")
  turns = set_difficulty()

  guess = 0
  while guess != number:
    print(f"  You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = guess_number(guess, number, turns)
    if turns == 0:
      print(f"  Sorry, no attempt left, the number you were looking for was {number}")
      return


keep_playing = True
while keep_playing == True:
  play()  
  continue_game = input("Would you like to replay? Type 'y' or 'n': ")
  if continue_game == 'y':
    clear()
  else:
    clear()
    print("Have a nice day! 🧚")
    keep_playing = False
