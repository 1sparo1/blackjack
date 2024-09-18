import random
import os

# Master Deck definition
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

# Unicode card symbols lookup
card_symbols = {
    "Hearts": {1: "🂱", 2: "🂲", 3: "🂳", 4: "🂴", 5: "🂵", 6: "🂶", 7: "🂷", 8: "🂸", 9: "🂹", 10: "🂺", 11: "🂻", 12: "🂽", 13: "🂾"},
    "Spades": {1: "🂡", 2: "🂢", 3: "🂣", 4: "🂤", 5: "🂥", 6: "🂦", 7: "🂧", 8: "🂨", 9: "🂩", 10: "🂪", 11: "🂫", 12: "🂭", 13: "🂮"},
    "Clubs": {1: "🃑", 2: "🃒", 3: "🃓", 4: "🃔", 5: "🃕", 6: "🃖", 7: "🃗", 8: "🃘", 9: "🃙", 10: "🃚", 11: "🃛", 12: "🃝", 13: "🃞"},
    "Diamonds": {1: "🃁", 2: "🃂", 3: "🃃", 4: "🃄", 5: "🃅", 6: "🃆", 7: "🃇", 8: "🃈", 9: "🃉", 10: "🃊", 11: "🃋", 12: "🃍", 13: "🃎"}
}

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def init():
    global GameDeck 
    temp = MasterDeck[:]  
    random.shuffle(temp)  
    GameDeck = temp  

def serve(num_cards=1):
    global GameDeck
    global player
    global Dealer
    
    # Deal 'num_cards' cards to the player and the dealer alternately
    for _ in range(num_cards):
        if GameDeck:
            card = GameDeck.pop(0)
            if card[1] == 1:
                card = handle_ace(card)
            player.append(card)  # Deal a card to the player
        if GameDeck:
            Dealer.append(GameDeck.pop(0))  # Deal a card to the dealer

def handle_ace(card):
    """Ask the player if they want the Ace to count as 1 or 11."""
    choice = input(f"You drew an Ace of {card[0]}. Would you like it to count as 1 or 11? ")
    if choice == "11":
        return (card[0], 11)
    return card

def card_value(card):
    """Calculate the value of a single card."""
    suit, value = card
    if value >= 10:  # Jack, Queen, King
        return 10
    return value

def hand_value(hand):
    """Calculate the total value of a hand."""
    return sum(card_value(card) for card in hand)

def bust(hand):
    """Check if a hand is bust (i.e., over 21)."""
    return hand_value(hand) > 21

def get_card_symbol(card):
    """Return the Unicode symbol for a given card."""
    suit, value = card
    return card_symbols[suit][value]

def print_hand_status():
    """Print the status of the player's hand with Unicode symbols and its value."""
    hand_symbols = " ".join(get_card_symbol(card) for card in player)
    print(f"Player's hand: {hand_symbols} Total: {hand_value(player)}")

def print_dealer_hand(hidden=True):
    """Print the dealer's hand, hiding the first card if needed."""
    if hidden:
        hand_symbols = f"🂠 {' '.join(get_card_symbol(card) for card in Dealer[1:])}"
        print(f"Dealer's hand: {hand_symbols} Total: ??")
    else:
        hand_symbols = " ".join(get_card_symbol(card) for card in Dealer)
        print(f"Dealer's hand: {hand_symbols} Total: {hand_value(Dealer)}")

game = True

while game:
    player = []
    Dealer = []
    init()
    clear_console()  # Clear the console before starting a new game
    print("Welcome to Blackjack")
    
    serve(2)  # Deal 2 cards each to player and dealer
    print_hand_status()
    print_dealer_hand(hidden=True)  # Dealer's hand, hide first card
    
    # Check initial bust
    if bust(player):
        print("Player busts!")
        break
    elif bust(Dealer):
        print("Dealer busts!")
        break

    playing = True
    while playing:
        response = input("Would you like to draw(1) or stand(2)? ").strip().lower()
        if response == "1" or response == "draw":
            serve(1)
            print_hand_status()
            print_dealer_hand(hidden=True)
            if bust(player):
                print("Player busts!")
                playing = False
                break
        elif response == "2" or response == "stand":
            playing = False

    if not bust(player):
        # Dealer hits if hand value is less than 17
        while hand_value(Dealer) < 17:
            Dealer.append(GameDeck.pop(0))  # Dealer draws until hand is 17 or higher
            clear_console()
            print("Dealer draws a card...")
            print_hand_status()
            print_dealer_hand(hidden=True)  # Still hide first card during dealer's draw
        
        # Dealer's final hand (reveal all cards)
        clear_console()
        print_hand_status()
        print_dealer_hand(hidden=False)  # Reveal all dealer cards at the end

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

    # Ask if the player wants to play again
    replay = input("Would you like to play again (y/n)? ").strip().lower()
    while replay not in ["y", "n"]:
        replay = input("Invalid input. Please enter 'y' or 'n': ").strip().lower()
    
    if replay == "n":
        game = False

print("Thank you for playing!")
