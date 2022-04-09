############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import replit
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card_list):
  
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0

  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose!"

  if user_score == computer_score:
    return "Draw"
  elif user_score == 0:
    return "BlackJack!! You win"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score == 0:
    return "Computer has BlackJack.. You lose!"
  elif computer_score > 21:
    return "You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, your current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      stand = input("Type 'y' to draw another card, or type 'n' to pass: ").lower()
      if stand == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    calculate_score(computer_cards)
    
  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play BlackJack..? Type 'y' for yes and 'n' fo no: ").lower() == 'y':
  replit.clear()
  play()