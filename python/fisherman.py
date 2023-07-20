import random
from dataclasses import dataclass
import collections

# Bools
yourTurn = True
start = True

# Integers
cardCount = 0

# Lists
cards = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Spades','Hearts','Diamonds','Leaves']
deck = []
yourBooks = []
opponentBooks = []
yourInventory = []
opponentInventory = []

stealingFrom = opponentInventory
stealingTo = yourInventory

# Strings
border = "--------------"

@dataclass(eq=True, frozen=True)
class Card:
        number: str
        suit: str

        def __str__(self):
                return f"{self.number} {self.suit}"

class InventoryInfo:
        def __init__(self, inventory):
                self.numbers = [c.number for c in inventory] # An array of your cards name e.g. ['Ace', 'Seven', 'Six', 'Five', 'Jack']
                self.dict = collections.Counter([c.number for c in inventory]) # A dictionary of all card names and amounts e.g. {'Ace': '1', 'Seven': '1', 'Six': '1', 'Five': '1', 'Jack': '1'}
                self.list = [f"{key}, x{value}" for key, value in collections.Counter([c.number for c in inventory]).items()] # An array of all of your cards e.g. ['Ace x1', 'Seven x1', 'Six x1', 'Five x1', 'Jack x1']
                self.card = [key for key, value in collections.Counter([c.number for c in inventory]).items()] # A card is the name of the card e.g. "Ace"
                self.amount = [value for key, value in collections.Counter([c.number for c in inventory]).items()] # Amount is the amount of a card e.g. "1"
                self.books = [key for key, value in collections.Counter([c.number for c in inventory]).items() if value >= 4] # A book is the key which has the value of or above 4

for card in cards:
        for suit in suits:
                deck.append(Card(card, suit))

random.shuffle(deck) # Shuffle

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

if start:
        for i in range(10): # Gives the players cards
                drawCard()
                if len(yourInventory) == 10:
                        opponentInventory = yourInventory[:5]
                        del yourInventory[:5] 
                        start = not start

def stealing():
        global yourTurn
        global cardCount
        global stealingFrom
        global stealingTo

        if not start and len(opponentInventory) == 0:
                print("You Win!")
        elif not start and len(yourInventory) == 0:
                print("You Lose!")

        if yourTurn:
                for cardAmount in yourInventoryInfo.amount:
                                cardCount += 1
                                if cardAmount == 4:
                                        print("You got a book!")
                                        
                                
                print(f"Opponent Books: {'   '.join(opponentBooks)}")
                print(f"Your Books: {'   '.join(yourInventoryInfo.books)}")
                print(f"Your inventory : {'   '.join(map(str, yourInventoryInfo.list))}")
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

        if any([asked.capitalize() == card.number for card in stealingTo]):
                if checkCard:
                        if yourTurn:
                                print("He had the card!")
                                print(border)
                        for x in stealingFrom:
                                if asked.capitalize() == x.number:
                                        stealingTo.append(x)
                                        stealingFrom.remove(x)
                else:
                        if yourTurn:
                                print("He didn't have the card. Go fish!")
                                print(border)
                        drawCard()
                        newCard = stealingTo[len(stealingTo) - 1].number

                        if newCard == asked.capitalize():
                                if yourTurn:
                                        print("You drew the card!")
                                        print(border)
                                else:
                                        print("Your opponent drew the card!")
                                        print(border)
                        else:
                                yourTurn = not yourTurn

                                if yourTurn:
                                        stealingFrom, stealingTo = opponentInventory, yourInventory
                                else:
                                        stealingFrom, stealingTo = yourInventory, opponentInventory
        else:
                print("Please enter a card that you have :/")
                print(border)        
        
while True: 
        # Objects
        yourInventoryInfo = InventoryInfo(yourInventory) # Your Inventory Info Object
        opponentInventoryInfo = InventoryInfo(opponentInventory) # Your Opponents Inventory Info Object

        print(yourInventoryInfo.amount, yourInventoryInfo.card)

        # Calls
        stealing()
