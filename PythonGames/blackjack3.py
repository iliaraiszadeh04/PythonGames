import random
import time

# Initialize the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

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

def display_hand(hand):
    for card in hand:
        time.sleep(0.5)
        print(f"{card['rank']} of {card['suit']}")

def play_game():
    player_score = 0
    dealer_score = 0
    
    while True:
        deck = create_deck()
        random.shuffle(deck)
        player_hand = []
        dealer_hand = []
        
        # Deal two cards to the player and two cards to the dealer
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        
        # Game loop
        while True:
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            
            print("\nPlayer's Hand:")
            display_hand(player_hand)
            print(f"Total Value: {player_value}")
            
            if player_value == 21:
                print("Blackjack! You win!")
                player_score += 1
                break
            elif player_value > 21:
                print("Bust! You lose.")
                dealer_score += 1
                break
            
            print("\nDealer's Hand:")
            print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
            
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            
            if action == 'hit':
                player_hand.append(deck.pop())
            elif action == 'stand':
                while dealer_value < 17:
                    dealer_hand.append(deck.pop())
                    dealer_value = calculate_hand_value(dealer_hand)
                
                print("\nDealer's Hand:")
                display_hand(dealer_hand)
                print(f"Total Value: {dealer_value}")
                
                if dealer_value > 21:
                    print("Dealer busts! You win!")
                    player_score += 1
                elif dealer_value > player_value:
                    print("Dealer wins!")
                    dealer_score += 1
                elif dealer_value == player_value:
                    print("It's a tie!")
                else:
                    print("You win!")
                    player_score += 1
                
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")
        
        print(f"Player's Score: {player_score}")
        print(f"Dealer's Score: {dealer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()