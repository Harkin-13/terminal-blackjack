import time
from deck import Deck
from player import Dealer
from player import Player

def show_hand(name, hand):
    print(f"\n{name}'s hand:")
    for card in hand:
        print(card)

# -----
# Setup
# -----
dealer = Dealer()
player = Player()
deck = Deck()

while True:
    start_game = input("Type 'play' to begin a new game: ").strip().lower()
    if start_game == "play":
        break

# ---------
# Game Loop
# ---------
while True:
    print("\n" + "-" * 40)
    dealer_score = 0
    player_score = 0
    player_bust = False
    round_over = False

    dealer.reset_hand()
    player.reset_hand()
    deck.reset_deck()

    # Dealer draws 2 cards
    dealer.draw_card(deck)
    dealer.draw_card(deck)

    time.sleep(1)

    # Reveal 1 dealer card
    print("\nDealer's Hand:")
    print(dealer.hand[0])
    print("Second card is face down")

    time.sleep(1)

    # Player draws 2 cards
    player.draw_card(deck)
    player.draw_card(deck)

    show_hand("Player", player.hand)
    
    player_score = player.get_score()
    print("Player score: ", player_score)

    time.sleep(1)

    # Check for early Blackjack
    dealer_score = dealer.get_score()
    if player_score == 21 and dealer_score == 21:
        print("\nYou and the dealer have Blackjack! It's a tie!")
        # Show dealer's full hand
        show_hand("Dealer", dealer.hand)
        round_over = True

    elif dealer_score == 21:
        print("\nDealer has Blackjack! You lose.")
        show_hand("Dealer", dealer.hand)
        round_over = True

    # -----------
    # Player Turn
    # -----------
    if not round_over:
        while True:

            # Check for blackjack (auto-win)
            if player_score == 21:
                print("Blackjack! You win!")
                show_hand("Dealer", dealer.hand)
                round_over = True
                break

            # Players enters 'hit' or 'stand'
            player_turn = input("Enter 'hit' or 'stand': ").strip().lower()
            if player_turn == 'hit':
                player.draw_card(deck)
                show_hand("Player", player.hand)

            # Determine player score
            player_score = player.get_score()
            print("Player score: ", player_score)

            # Player bust logic
            if player_score > 21:
                print("You bust!")
                player_bust = True
                break

            # when player stands
            if player_turn == 'stand':
                break
        
        time.sleep(1)

        if player_bust:
            show_hand("Dealer", dealer.hand)
            print("Dealer wins!")
            round_over = True
        
        # ------------
        # Dealer Logic
        # ------------
        if not round_over:
            # Reveal Dealer hand
            show_hand("Dealer", dealer.hand)

            # Dealer draws more if total < 17
            while dealer_score < 17:
                dealer.draw_card(deck)
                print("Dealer draws:", dealer.hand[-1])
                dealer_score = dealer.get_score()

            # Dealer bust logic
            if dealer_score > 21:
                print("Dealer busts!")
                print("You win!")
            elif player_score > dealer_score:
                print("You win!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")

    # Final Score
    print(f"\nFinal Scores — You: {player_score} | Dealer: {dealer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break