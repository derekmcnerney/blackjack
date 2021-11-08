import random

class Card:
    def __init__(self, suit, value, card_value):        
        self.suit = suit       
        self.value = value      
        self.card_value = card_value


def print_cards(cards, hidden):    
    s = ""
    for card in cards:       
        s = s + " {} ".format(card.value)
    if hidden:
        s += "?"
    print(s)
    s = ""
    for card in cards:
        s = s + " {} ".format(card.suit)
    if hidden:
        s += "?"
    print(s)

    print()

def blackjack_game(deck):   
    player_cards = []
    dealer_cards = []  
    player_score = 0
    dealer_score = 0

    while len(player_cards) < 2:
        
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)       
        player_score += player_card.card_value

        print("Your cards: ")
        print_cards(player_cards, False)
        print("Your score = ", player_score)

        input("Press Enter to continue")
       
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("Dealer cards: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("Dealer score = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("Dealer score = ", dealer_score -
                  dealer_cards[-1].card_value)
       
        input("Press Enter to continue")

    if player_score == 21:
        print("You got a blackjack!! ")
        print("You win!!")
        quit()

    print("Dealer cards: ")
    print_cards(dealer_cards[:-1], True)
    print("Dealer score = ", dealer_score - dealer_cards[-1].card_value)

    print("Press Enter to continue")

    print("Your cards: ")
    print_cards(player_cards, False)
    print("Your score = ", player_score)


    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")

        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            
            print("Wrong choice!! Try Again")

        if choice.upper() == 'H':

            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            player_score += player_card.card_value

            print("Dealer cards: ")
            print_cards(dealer_cards[:-1], True)
            print("Dealer score = ", dealer_score -
                  dealer_cards[-1].card_value)

            print()

            print("Your cards: ")
            print_cards(player_cards, False)
            print("Your score = ", player_score)

        if choice.upper() == 'S':
            break

    
    print("Your cards: ")
    print_cards(player_cards, False)
    print("Your score = ", player_score)

    print()
    
    print("Dealer cards: ")
    print_cards(dealer_cards, False)
    print("Dealer score = ", dealer_score)


    if player_score == 21:
        print("You got a Blackjack. You win!")
        quit()


    if player_score > 21:
        print("You busted. You lose.")
        quit()

    input("Press Enter to continue")

    while dealer_score < 17:
        

        print("Dealer has hit.")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("Your cards: ")
        print_cards(player_cards, False)
        print("Your score = ", player_score)

        print()

        print("Dealer cards: ")
        print_cards(dealer_cards, False)
        print("Dealer score = ", dealer_score)

        input("Press Enter to continue")

    if dealer_score > 21:
        print("Dealer busted. You win!!")
        quit()

    if dealer_score == 21:
        print("Dealer got a Blackjack!! You lose")
        quit()

    if dealer_score == player_score:
        print("Tie game!")

    elif player_score > dealer_score:
        print("You Win!!")

    else:
        print("Dealer wins :(")


if __name__ == '__main__':

    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    suits_values = {"Spades": "♠️", "Hearts": "♥️",  

                    "Clubs": "♣️", "Diamonds": "♦️"}

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


    cards_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    deck = []

    for suit in suits:

        for card in cards:

            deck.append(Card(suits_values[suit], card, cards_values[card]))

    blackjack_game(deck)
