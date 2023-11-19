import random
from dataclasses import dataclass
import collections


# Arrays
cards = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Spades','Hearts','Diamonds','Leaves']
deck = []
your_books = []
opponent_books = []
your_inventory = []
opponent_inventory = []
stealing_from = opponent_inventory
stealing_to = your_inventory

# Bools
your_turn = True
start = True

# Integers
card_count = 0

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

def draw_card(): # Draws a card
    random_card = random.randint(0,len(deck) - 1)

    if your_turn:
            your_inventory.append(deck[random_card])
            if not start:
                print(f"You got {deck[random_card]}!")
                print(border)
            deck.remove(deck[random_card])

    if not your_turn:
            opponent_inventory.append(deck[random_card])
            deck.remove(deck[random_card])

if start:
        for i in range(10): # Gives the players cards
                draw_card()
                if len(your_inventory) == 10:
                        opponent_inventory = your_inventory[:5]
                        del your_inventory[:5] 
                        start = not start

def stealing():
        global your_turn
        global card_count
        global stealing_from
        global stealing_to

        if not start and len(opponent_inventory) == 0:
                print("You Win!")
        elif not start and len(your_inventory) == 0:
                print("You Lose!")

        if your_turn:
                for card_amount in your_inventory_info.amount:
                                card_count += 1
                                if card_amount == 4:
                                        print("You got a book!")
                                        
                                
                print(f"Opponent Books: {'   '.join(opponent_books)}")
                print(f"Your Books: {'   '.join(your_inventory_info.books)}")
                print(f"Your inventory : {'   '.join(map(str, your_inventory_info.list))}")
                print(border)
                
                asked = input("Please write the card you want to steal : ")
                print(border)
                check_card = any([asked.capitalize() == card.number for card in stealing_from])
        else:
                ai_asking = random.randint(0, len(opponent_inventory) - 1)
                asked = opponent_inventory[ai_asking].number
                check_card = any([asked.capitalize() == card.number for card in stealing_from])
                print(f'AI: {asked}')
                print(border)

        if any([asked.capitalize() == card.number for card in stealing_to]):
                if check_card:
                        if your_turn:
                                print("He had the card!")
                                print(border)
                        for x in stealing_from:
                                if asked.capitalize() == x.number:
                                        stealing_to.append(x)
                                        stealing_from.remove(x)
                else:
                        if your_turn:
                                print("He didn't have the card. Go fish!")
                                print(border)
                        draw_card()
                        new_card = stealing_to[len(stealing_to) - 1].number

                        if new_card == asked.capitalize():
                                if your_turn:
                                        print("You drew the card!")
                                        print(border)
                                else:
                                        print("Your opponent drew the card!")
                                        print(border)
                        else:
                                your_turn = not your_turn

                                if your_turn:
                                        stealing_from, stealing_to = opponent_inventory, your_inventory
                                else:
                                        stealing_from, stealing_to = your_inventory, opponent_inventory
        else:
                print("Please enter a card that you have :/")
                print(border)        
        
while True: 
        # Objects
        your_inventory_info = InventoryInfo(your_inventory) # Your Inventory Info Object
        opponent_inventory_info = InventoryInfo(opponent_inventory) # Your Opponents Inventory Info Object

        print(your_inventory_info.amount, your_inventory_info.card)

        # Calls
        stealing()