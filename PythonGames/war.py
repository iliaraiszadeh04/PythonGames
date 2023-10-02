import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def play_war():
    print("Welcome to the card game 'War' against the computer!")
    deck = create_deck()

    player_deck = deck[:26]
    computer_deck = deck[26:]

    while True:
        input("Press Enter to draw a card...")

        player_card = player_deck.pop(0)
        computer_card = computer_deck.pop(0)

        print(f"Your card: {player_card['rank']} of {player_card['suit']}")
        print(f"Computer's card: {computer_card['rank']} of {computer_card['suit']}")

        player_rank_index = ranks.index(player_card['rank'])
        computer_rank_index = ranks.index(computer_card['rank'])

        if player_rank_index > computer_rank_index:
            print("You win this round!")
            player_deck.extend([player_card, computer_card])
        elif player_rank_index < computer_rank_index:
            print("Computer wins this round!")
            computer_deck.extend([player_card, computer_card])
        else:
            print("It's a tie! War begins...")

            if len(player_deck) < 4 or len(computer_deck) < 4:
                print("Insufficient cards for a war. The game is a draw.")
                break

            player_war_cards = player_deck[:4]
            computer_war_cards = computer_deck[:4]

            player_card = player_deck.pop(0)
            computer_card = computer_deck.pop(0)

            player_rank_index = ranks.index(player_card['rank'])
            computer_rank_index = ranks.index(computer_card['rank'])

            if player_rank_index > computer_rank_index:
                print("You win the war!")
                player_deck.extend(player_war_cards + [player_card, computer_war_cards, computer_card])
            elif player_rank_index < computer_rank_index:
                print("Computer wins the war!")
                computer_deck.extend(player_war_cards + [player_card, computer_war_cards, computer_card])
            else:
                print("It's another tie!")

        print(f"You have {len(player_deck)} cards. Computer has {len(computer_deck)} cards.")

        if not player_deck:
            print("You ran out of cards. Computer wins!")
            break
        elif not computer_deck:
            print("Computer ran out of cards. You win!")
            break

if __name__ == "__main__":
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    play_war()