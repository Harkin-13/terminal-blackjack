import random

# Card + Deck classes
# -------------------

# Intialise lists for building cards
rank_list = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.played = False

        # Assign default value to face cards
        if str(rank) in ['J', 'Q', 'K']:
            self.value = 10
        elif rank == 'A':
            self.value = 11
        else:
            self.value = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

#  Creates and stores all 52 Card objects
class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in suit_list:
            for rank in rank_list:
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def shuffle(self):
        while True:
            random_card = random.choice(self.cards)
            if not random_card.played:
                random_card.played = True
                return random_card
            
    def reset_deck(self):
        for card in self.cards:
            card.played = False