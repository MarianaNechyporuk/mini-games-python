import random
from art import logo
from replit import clear

def computer():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def count_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def checking(player_count, computer_count):
  if player_count > 21 and computer_count > 21:
    return "Too much, you lose"

    
  if computer_count > 21:
    return "Computer is over. You win"
  elif player_count > 21:
    return "More then 21. You lose"
  elif computer_count == 0:
    return "Computer have BlackJack! You lose!"
  elif player_count == 0:
    return "BlackJack! You win!"
  elif computer_count == 0 and player_count == 0:
    return "Omg! You both have BlackJack!" 
  elif computer_count == player_count:
    return "Equal with computer. Try again" 
  elif player_count > computer_count:
    return "You win!"
  else:
    return "You lose"


def game():
  
  print(logo)
  
  player_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    player_cards.append(computer())
    computer_cards.append(computer())

  while not game_over:
    player_count = count_score(player_cards)
    computer_count = count_score(computer_cards)
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    if player_count == 0 or computer_count == 0 or player_count > 21:
      game_over = True
    else:
        new_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_cards == "y":
          player_cards.append(computer())
        else:
          game_over = True

  while computer_count != 0 and computer_count < 17:
    computer_cards.append(computer())
    computer_count = count_score(computer_cards)

  print(f"Your final hand: {player_cards}")
  print(f"Computer's final hand: {computer_cards}")
  print(checking(player_count, computer_count))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  game()
