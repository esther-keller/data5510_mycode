#import stuff
from DeckOfCards import *

#figure out score calculation because ace's suck
def calculate_score(hand):
    #starting values
    score = 0
    ace_count = 0

    for card in hand:
        score += card.val
        if card.face == "Ace":
            ace_count += 1
    while score > 21 and ace_count > 0:
        score -=10
        ace_count -= 1
    return score

#Display Welcome Message
print('Welcome to my terminal! Today we will play BlackJack!')
print('------------------')
print() #spacing like this is used periodically to break up the text
print()

#create variables 
play_again = 'y'
num_times_played = 0
games_won = 0
games_lost = 0
deck = DeckOfCards()

#begin while loop to start/restart the game
while play_again == 'y':
    num_times_played += 1
    #before shuffle:
    print("Confirm New Deck:")
    deck.print_deck()
    print()
    print()
    #confirm shuffle:
    deck.shuffle_deck()
    print('Confirm Shuffle Deck:')
    deck.print_deck()
    print()
    print()

    #create hand lists and start their scores
    dealer_hand = []
    player_hand = []
    dealer_score = 0
    player_score = 0
    player_busted = False

    #deal 2 cards and append to list
    player_hand.append(deck.get_card()) #get card 1
    player_hand.append(deck.get_card()) #get card 2
    dealer_hand.append(deck.get_card()) #card 1
    dealer_hand.append(deck.get_card()) #card 2


    print("Card 1: ", player_hand[0])
    print("Card 2: ", player_hand[1])

    player_score = calculate_score(player_hand)
    print("Your score is: ",player_score)
    print()

    #create hit loop
    while player_score <= 21:
        hit = input("Would you like to hit? (y/n): ").lower()
        if hit == 'y':
            #deal 1 new card + recalculate score
            player_hand.append(deck.get_card())
            print("Card", len(player_hand), ":", player_hand[-1]) #come back to this and figure out how to not hard code "card 3, card 4" etc
            player_score = calculate_score(player_hand)
            print("Your score is: ",player_score)
            print()
            if player_score > 21:
                print("You busted! You lose!")
                games_lost += 1
                player_busted = True
                break
        elif hit == 'n':
            #end and print the score for them
            print()
            print("Final score = ", player_score)
            break
        else: 
            print("Invalid-- try again (y/n)")
            print()

    #dealer logic
    if player_busted == False:
        print("Dealer card 1: ", dealer_hand[0])
        print("Dealer card 2: ", dealer_hand[1])
        print("Dealer score: ", calculate_score(dealer_hand))
        print()
        dealer_score = calculate_score(dealer_hand)

        while dealer_score < 17:
            dealer_hand.append(deck.get_card())
            dealer_score = calculate_score(dealer_hand)
            print("Dealer hits: ", dealer_hand[-1])
            print("Dealer score:",dealer_score)
            print()

        #comparison logic - who wins?
    if dealer_score > 21:
        print("Dealer busted, YOU WIN!!!!!!!")
        print("Dealer's Final Score: ", dealer_score)
        print("Your Final Score: ", player_score)
        games_won += 1
    elif player_score > dealer_score:
        print("Your score is higher, YOU WIN!!!!!!!!")
        print("Dealer's Final Score: ", dealer_score)
        print("Your Final Score: ", player_score)
        games_won += 1
    else: 
            print("Dealer score is equal to or higher than your score, so YOU LOSE!!!!!!")
            print("Dealer's Final Score: ", dealer_score)
            print("Your Final Score: ", player_score)
            games_lost += 1

    #ask if they want to play more games
    play_again = input("Would you like to play again? (y/n)").lower()
    if play_again == 'n':
        print("---------------")
        print('Total # of games played: ',num_times_played)
        print("Total # of games won: ", games_won)
        print("Total # of games lost: ", games_lost)
        print("Win/Loss percentage: ", round(((games_won / num_times_played)*100),2),"%")
        print()
        print('Thanks for playing today!')