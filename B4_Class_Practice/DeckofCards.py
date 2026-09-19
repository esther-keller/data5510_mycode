'''----------Notes----------

'''

import random
class Card(): #supportive class becuase it's used by the deck of cards class
    def __init__(self, suit, face, value): #constructer line
        self.suit = suit
        self.face = face
        self.value = value
    def __str__(self):
        return self.face + ' of ' + self.suit + ', value: ' + str(self.value)

class DeckOfCards(): #best practice for variables+function names is to use _ to seperate words, but for classes, best practice is to use CamelCase
    def __init__(self): #this is the constructer line
        self.deck = []
        self.suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs'] 
        self.faces = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace'] # I want this to be homogeneous data so I'm making them all strings
        self.values = [2,3,4,5,6,7,8,9,10,11]
        self.play_idx = 0

        for suite in self.suites:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit,self.faces[i],self.values[i]))

    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.play_idx = 0

    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit, end=', ')
        print('-------------')

    def get_card(self):
        self.play_idx += 1
        return self.deck[self.play_idx -1]