import random

# Define the master deck with unique keys for suits and card values
MasterDeck = [
    ("Hearts", 1), ("Hearts", 2), ("Hearts", 3), ("Hearts", 4), ("Hearts", 5),
    ("Hearts", 6), ("Hearts", 7), ("Hearts", 8), ("Hearts", 9), ("Hearts", 10),
    ("Hearts", 10), ("Hearts", 10), ("Hearts", 10),
    ("Spades", 1), ("Spades", 2), ("Spades", 3), ("Spades", 4), ("Spades", 5),
    ("Spades", 6), ("Spades", 7), ("Spades", 8), ("Spades", 9), ("Spades", 10),
    ("Spades", 10), ("Spades", 10), ("Spades", 10),
    ("Clubs", 1), ("Clubs", 2), ("Clubs", 3), ("Clubs", 4), ("Clubs", 5),
    ("Clubs", 6), ("Clubs", 7), ("Clubs", 8), ("Clubs", 9), ("Clubs", 10),
    ("Clubs", 10), ("Clubs", 10), ("Clubs", 10),
    ("Diamonds", 1), ("Diamonds", 2), ("Diamonds", 3), ("Diamonds", 4), ("Diamonds", 5),
    ("Diamonds", 6), ("Diamonds", 7), ("Diamonds", 8), ("Diamonds", 9), ("Diamonds", 10),
    ("Diamonds", 10), ("Diamonds", 10), ("Diamonds", 10)
]

GameDeck = []

def init():
    global GameDeck  # Use the global GameDeck variable
    temp = MasterDeck[:]  # Create a copy of the MasterDeck
    random.shuffle(temp)  # Shuffle the copy
    GameDeck = temp  # Assign the shuffled deck to GameDeck

def serve(num_cards=1):
    global GameDeck
    global player
    global Dealer
    
    # Deal 'num_cards' cards to the player and the dealer alternately
    for _ in range(num_cards):
        if GameDeck:
            player.append(GameDeck.pop(0))  # Deal a card to the player
        if GameDeck:
            Dealer.append(GameDeck.pop(0))  # Deal a card to the dealer

def card_value(card):
    """Calculate the value of a single card."""
    suit, value = card
    if value >= 10:  # Jack, Queen, King
        return 10
    return value

def hand_value(hand):
    """Calculate the total value of a hand."""
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[1] == 1)
    
    # Adjust for Aces value
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1
    
    return total

def bust(hand):
    """Check if a hand is bust (i.e., over 21)."""
    return hand_value(hand) > 21

game = True
player = []
Dealer = []

while game:
    init()
    print("Welcome to Blackjack")
    serve(2)  # Deal 2 cards each to player and dealer
    #print("Dealer's hand:", Dealer)
    print("Player's hand:", player)
    
    # Check initial bust
    if bust(player):
        print("Player busts!")
        break
    elif bust(Dealer):
        print("Dealer busts!")
        break

    playing = True
    while playing:
        response = input("Would you like to draw or stand (y/n)? ").strip().lower()
        if response == "y":
            serve(1)
            print("Player's hand:", player)
            if bust(player):
                print("Player busts!")
                playing = False
                break
        elif response == "n":
            playing = False

    if not bust(player):
        while hand_value(Dealer) < 17:
            serve(1)
        print("Dealer's hand:", Dealer)
        if bust(Dealer):
            print("Dealer busts!")
        else:
            player_total = hand_value(player)
            dealer_total = hand_value(Dealer)
            if player_total > dealer_total:
                print("Player wins!")
            elif player_total < dealer_total:
                print("Dealer wins!")
            else:
                print("It's a tie!")

    game = False  # End the game loop after one iteration for demonstration

