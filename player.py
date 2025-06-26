from deck import Card
from deck import Deck

# Player and Dealer class
# -----------------------

class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        card = deck.shuffle()
        self.hand.append(card)

    def get_score(self):
        total = 0
        ace_count = 0

        for card in self.hand:
            total += card.value
            if card.rank == 'A':
                ace_count += 1

        # Convert Aces from 11 to 1 if we're over 21
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total
    
    def reset_hand(self):
        self.hand = []
            

class Dealer:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        card = deck.shuffle()
        self.hand.append(card)

    def get_score(self):
        total = 0
        ace_count = 0

        for card in self.hand:
            total += card.value
            if card.rank == 'A':
                ace_count += 1

        # Convert Aces from 11 to 1 if we're over 21
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total
    
    def reset_hand(self):
        self.hand = []