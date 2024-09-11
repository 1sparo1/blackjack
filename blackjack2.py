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
random.shuffle(cards)
print("Let's play blackjack!")
def isInt(char):
    try: 
        int(char)
        return True
    except:
        return False
def calculateScore(deck):
    score = 0
    aCount = 0
    for card in deck:
        card = card[1:]
        
        if isInt(card):
            score += int(card)
        elif card != "A":
            score += 10
        else:
            aCount += 1
    score += aCount
    if score < 12 and aCount > 0:
        score += 10
    return score
def askPlayer():
    a = input("Would you like to draw or stand?")
    if a == "draw":
        return True
    elif a == "stand":
        return False
    else:
        print("Say either draw or stand.")
        return askPlayer()
dealerDeck = []
dealerDeck.append(cards.pop())
dealerDeck.append(cards.pop())
playerDeck = []
playerDeck.append(cards.pop())
playerDeck.append(cards.pop())
while calculateScore(dealerDeck) < 17:
    dealerDeck.append(cards.pop())
if calculateScore(dealerDeck) > 21:
    print("Dealer busts, you win!")
    exit(3)
def playBlackJack():
    
    print("Here is your deck: " + str(playerDeck))
    if calculateScore(playerDeck) > 21:
        print("You busted.")
        exit(3)
    if calculateScore(playerDeck) == 21:
        if calculateScore(dealerDeck) == 21:
            print("You tie.")
        else:
            print("You win!")
        exit(3)
    didDraw = askPlayer()
    if didDraw == True:
        playerDeck.append(cards.pop())
        print("You drew " + str(playerDeck[-1]))
        playBlackJack()
    else:
        if calculateScore(playerDeck) > calculateScore(dealerDeck):
            print("You win!")
            
        elif calculateScore(playerDeck) < calculateScore(dealerDeck):
            print("You lose")
        else:
            print("Tie")
        print("The dealer's deck " + str(dealerDeck))
        exit(3)
#print(isInt("11"))
playBlackJack()
