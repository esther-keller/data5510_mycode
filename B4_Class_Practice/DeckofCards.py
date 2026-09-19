'''----------Notes----------

'''

import random
class Card(): #supportive class becuase it's used by the deck of cards class
    def __init__(self, suit, face): #constructer line
        self.suit = suit
        self.face = face

class DeckOfCards(): #best practice for variables+function names is to use _ to seperate words, but for classes, best practice is to use CamelCase
    def __init__(self, deck=[]): #this is the constructer line
        self.deck = deck

    def shuffle_deck(self):
        random.shuffle(self.deck)
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit)

suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs'] 
faces = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace'] # I want this to be homogeneous data so I'm making them all strings
cards = []
for suite in suites:
    for face in faces:
        cards.append(Card(suite,face))
deck = DeckOfCards(cards) #calling the donstructer again

deck.print_deck() #this should be my full deck of 52 cards
deck.shuffle_deck()
print('-------------')
deck.print_deck()