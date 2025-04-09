import random
from art import logo

easy = 10
hard = 5

def answer(guess, number, turns):
    if guess < number:
      print("Too low")
      return turns - 1
    elif guess > number:
      print("Too high")
      return turns - 1
    else:
      print(f"Yes! You win! Your number was {number}")

def how_hard():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return easy
  elif difficulty == 'hard':
    return hard
  else:
    raise SyntaxError('THIS IS A ERROR')

def game():
  
  print(logo)
  print('''Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.''')
  number = random.randint(1, 100)
  #print(f"Hint: {number}")

  turns = how_hard()

  guess = 0
  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess : "))
    turns = answer(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")

 
game()