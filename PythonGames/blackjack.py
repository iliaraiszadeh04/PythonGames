import random
import time

# Initialize the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Initialize player and dealer hands
player_hand = []
dealer_hand = []

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        rank = card['rank']
        if rank in ['King', 'Queen', 'Jack']:
            value += 10
        elif rank == 'Ace':
            value += 11
            num_aces += 1
        else:
            value += ranks.index(rank) + 2
    
    # Handle Aces
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

# Function to display a hand
def display_hand(hand):
    for card in hand:
        time.sleep(1)
        print(f"{card['rank']} of {card['suit']}")

# Deal two cards to the player and two cards to the dealer
for _ in range(2):
    player_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
    dealer_hand.append(deck.pop(random.randint(0, len(deck) - 1)))

# Game loop
while True:
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    print("\nPlayer's Hand:")
    display_hand(player_hand)
    print(f"Total Value: {player_value}")
    
    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break
    
    print("\nDealer's Hand:")
    print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
    
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    
    if action == 'hit':
        player_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
    elif action == 'stand':
        while dealer_value < 17:
            dealer_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
            dealer_value = calculate_hand_value(dealer_hand)
        
        print("\nDealer's Hand:")
        display_hand(dealer_hand)
        print(f"Total Value: {dealer_value}")
        
        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif dealer_value >= player_value:
            print("Dealer wins!")
        else:
            print("You win!")
        
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")