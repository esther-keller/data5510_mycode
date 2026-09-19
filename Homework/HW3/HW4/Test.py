'---------test---------'
import random

# Card class
class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f"{self.face} of {self.suit}"


# Deck of Cards class
class DeckOfCards:
    def __init__(self):
        self.deck = []

        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

        self.faces = [
            '2', '3', '4', '5', '6', '7', '8', '9', '10',
            'Jack', 'Queen', 'King', 'Ace'
        ]

        self.values = [
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            10, 10, 10, 11
        ]

        self.play_idx = 0

        # Create 52 cards
        for suit in self.suits:
            for i in range(len(self.faces)):
                self.deck.append(
                    Card(suit, self.faces[i], self.values[i])
                )

    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.play_idx = 0

    def get_card(self):
        if self.play_idx >= len(self.deck):
            raise Exception("No more cards in deck!")

        card = self.deck[self.play_idx]
        self.play_idx += 1
        return card


# Create and shuffle deck
deck = DeckOfCards()
deck.shuffle_deck()

# Deal initial two cards
card1 = deck.get_card()
card2 = deck.get_card()

print("Your cards:")
print(card1)
print(card2)

score = card1.value + card2.value

print("\nYour score is:", score)

# Check for starting blackjack
if score == 21:
    print("Blackjack! You win!")

else:

    # Keep asking until stand, 21, or bust
    while score < 21:

        hit = input("\nWould you like to hit? (y/n): ")

        if hit.lower() == 'y':

            new_card = deck.get_card()

            print("\nYou drew:")
            print(new_card)

            score += new_card.value

            print("New Score:", score)

            if score > 21:
                print("Bust! You lose.")
                break

            elif score == 21:
                print("Blackjack! You win!")
                break

        else:
            print("You stand with a score of", score)
            break