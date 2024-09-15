import random
cards = []
#initializes each class of cards
classes = ["S","C","H","D"]
#creates 13 cards for each class
for clas in classes:
    #adds all number cards and face cards
    cards.append(clas + "A")
    for number in range(2,11):
        cards.append(clas + str(number))
    cards.append(clas + "J")
    cards.append(clas + "Q")
    cards.append(clas + "K")
#shuffles cards
random.shuffle(cards)
print("Let's play blackjack!")

#checks if character is integer
def isInt(char):
    try: 
        int(char)
        return True
    except:
        return False
#calculates scores
def calculateScore(deck):
    score = 0
    aCount = 0
    for card in deck:
        card = card[1:]
        #if number card just add the number
        if isInt(card):
            score += int(card)
        #if its not a number and not an ace add 10(King,Queen,Jack)
        elif card != "A":
            score += 10
        #count Aces
        else:
            aCount += 1
    #adds all aces as ones
    score += aCount
    if score < 12 and aCount > 0:
        #if the score is 11 or under and you have aces you can add 10
        score += 10
    return score
#asks the player if they wanna draw or stand until they put one or the other
def askPlayer():
    a = input("Would you like to draw or stand? ")
    if a == "draw":
        return True
    elif a == "stand":
        return False
    else:
        print("Say either draw or stand.")
        return askPlayer()
#initializes hands of delear and player, giving each 2 cards
dealerHand = []
dealerHand.append(cards.pop())
dealerHand.append(cards.pop())
playerHand = []
playerHand.append(cards.pop())
playerHand.append(cards.pop())
#dealer draws until score exceeds 17
while calculateScore(dealerHand) < 17:
    dealerHand.append(cards.pop())
#if dealer busts player wins
if calculateScore(dealerHand) > 21:
    print("Dealer busts, you win!")
    exit(3)
def playBlackJack():
    
    print("Here is your deck: " + str(playerHand))
    #checks score to see if player busts or wins
    if calculateScore(playerHand) > 21:
        print("You busted.")
        return
    if calculateScore(playerHand) == 21:
        if calculateScore(dealerHand) == 21:
            print("You tie.")
        else:
            print("You win!")
        print("The dealer's deck is " + str(dealerHand))
        return
    #asks player whether they wanna stand or draw
    didDraw = askPlayer()
    if didDraw == True:
        #draws a card
        playerHand.append(cards.pop())
        print("You drew " + str(playerHand[-1]))
        #recursive game loop
        playBlackJack()
    else:
        if calculateScore(playerHand) > calculateScore(dealerHand):
            #better score than dealer means you win
            print("You win!")
            
        elif calculateScore(playerHand) < calculateScore(dealerHand):
            #Worse score means you lose
            print("You lose")
        else:
            #same score means tie
            print("Tie")
        print("The dealer's deck is " + str(dealerHand))
        return

playBlackJack()
