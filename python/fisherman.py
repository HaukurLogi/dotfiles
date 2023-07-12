import random
from dataclasses import dataclass
import collections

@dataclass(eq=True, frozen=True)
class Card:
        number: str
        suit: str

        def __str__(self):
                return f"{self.number} {self.suit}"

# Lists
cards = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Spades','Hearts','Diamonds','Leaves']
deck = []
yourBooks = []
opponentBooks = []
duplicates = []
yourInventory = []
opponentInventory = []

for card in cards:
        for suit in suits:
                deck.append(Card(card, suit))

random.shuffle(deck) # Shuffle

# Bools
yourTurn = True
start = True

# Other variables
border = "--------------"

def drawCard(): # Draws a card
    randomCard = random.randint(0,len(deck) - 1)

    if yourTurn:
            yourInventory.append(deck[randomCard])
            if not start:
                print(f"You got {deck[randomCard]}!")
                print(border)
            deck.remove(deck[randomCard])

    if not yourTurn:
            opponentInventory.append(deck[randomCard])
            deck.remove(deck[randomCard])

for i in range(10): # Gives the players cards
        drawCard()
        if len(yourInventory) == 10:
                opponentInventory = yourInventory[:5]
                del yourInventory[:5] 
                start = not start

def turns():
        global stealingFrom
        global notstealingFrom

        if yourTurn:
                stealingFrom = opponentInventory
                notstealingFrom = yourInventory
        else:
                stealingFrom = yourInventory
                notstealingFrom = opponentInventory

def stealing():
        global yourTurn

        if yourTurn:
                InventoryNumbers = [c.number for c in notstealingFrom]
                counterDict = collections.Counter(InventoryNumbers)
                counterList = [f"{key}, x{value}" for key, value in counterDict.items()]

                for value in counterDict.items():
                        if value == 4:
                                print("You have book")
                print(f"Opponent Books: {'   '.join(opponentBooks)}")
                print(f"Your Books: {'   '.join(yourBooks)}")
                print(f"Your inventory : {'   '.join(map(str, counterList))}")
                print(border)
                
                asked = input("Please write the card you want to steal : ")
                print(border)
                checkCard = any([asked.capitalize() == card.number for card in stealingFrom])
        else:
                aiAsking = random.randint(0, len(opponentInventory) - 1)
                asked = opponentInventory[aiAsking].number
                checkCard = any([asked.capitalize() == card.number for card in stealingFrom])
                print(f'AI: {asked}')
                print(border)


        if any([asked.capitalize() == card.number for card in notstealingFrom]):
                if checkCard:
                        if yourTurn:
                                print("He had the card!")
                                print(border)
                        for x in stealingFrom:
                                if asked.capitalize() == x.number:
                                        notstealingFrom.append(x)
                                        stealingFrom.remove(x)
                else:
                        if yourTurn:
                                print("He didn't have the card. Go fish!")
                                print(border)
                        drawCard()
                        newCard = notstealingFrom[len(notstealingFrom) - 1].number

                        if newCard == asked.capitalize():
                                if yourTurn:
                                        print("You drew the card!")
                                        print(border)
                                else:
                                        print("Your opponent drew the card!")
                                        print(border)
                        else:
                                yourTurn = not yourTurn
        else:
                print("Please enter a card that you have :/")
                print(border)        
        
while True:
        turns()
        stealing()