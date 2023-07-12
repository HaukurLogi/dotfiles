import random

cards = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Spades','Hearts','Diamonds','Leaves']
shuffledCardsWithDuplicates = []
yourInventory = []
opponentInverntory = []

from dataclasses import dataclass

@dataclass
class Card:
        number: str
        suit: str

        def __str__(self):
                return f"{self.number} {self.suit}"

deck = []

for card in cards:
        for suit in suits:
                deck.append(Card(card, suit))

random.shuffle(deck) # Shuffle

print('  '.join(map(str, deck)))