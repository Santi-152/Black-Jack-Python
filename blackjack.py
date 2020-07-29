import random
import sys

J = 10
Q = 10
K = 10
A = 1 
deck = 4 * ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A])

dealerHand = []
playerHand = []
dealerTotal = 0
playerTotal = 0

def drawCardDealer(): 
    global dealerHand
    global playerHand
    global dealerTotal
    global playerTotal
    global deck
    cardD = random.choice(deck)
    if cardD == J:
        dealerHand.append("J")
        dealerTotal += 10
        deck.remove(J)
    elif cardD == Q:
        dealerHand.append("Q")
        dealerTotal += 10
        deck.remove(Q)
    elif cardD == K:
        dealerHand.append("K")
        dealerTotal += 10
        deck.remove(K)
    elif cardD == A:
        dealerHand.append("A")
        deck.remove(A)
        if dealerTotal <= 10: 
            dealerTotal += 11
        elif dealerTotal > 10 and dealerTotal < 21:
            dealerTotal += 1
    else:
        dealerHand.append(cardD)
        dealerTotal += cardD
        deck.remove(cardD)
    return cardD

def drawCardPlayer():
    global dealerHand
    global playerHand
    global dealerTotal
    global playerTotal
    global deck
    cardP = random.choice(deck)
    if cardP == J:
        playerHand.append("J")
        playerTotal += 10
        deck.remove(J)
    elif cardP == Q:
        playerHand.append("Q")
        playerTotal += 10
        deck.remove(Q)
    elif cardP == K:
        playerHand.append("K")
        playerTotal += 10
        deck.remove(K)
    elif cardP == A:
        playerHand.append("A")
        deck.remove(A)
        if playerTotal <= 10:
            playerTotal += 11
        elif playerTotal > 10 and playerTotal < 21:
            playerTotal += 1
    else:
        playerHand.append(cardP)
        playerTotal += cardP
        deck.remove(cardP)
    return cardP

def hit():
        global dealerHand
        global playerHand
        drawCardPlayer()
        print("Dealer: ", dealerHand, "Count: ", dealerTotal)
        print("Player: ", playerHand, "Count: ", playerTotal,"\n")

def stand():
        global dealerHand
        global dealerTotal
        global A
        drawCardDealer()
        if dealerHand == [10, "A"] or dealerHand == ["A", 10]:
            print("Dealer has BLACKJACK!")
            playAgain()    
        while dealerTotal < 17:
            drawCardDealer()
        if dealerTotal >= 17:
            print("Dealer: ", dealerHand, "Count: ", dealerTotal)
            print("Player: ", playerHand, "Count: ", playerTotal,"\n")
            if dealerTotal == 21 and dealerTotal != playerTotal:
                print("Dealer WINS!\n")
                playAgain()
            elif dealerTotal > 21:
                print("Dealer BUSTED!\n")
                playAgain()
            elif dealerTotal < 21 and dealerTotal > playerTotal:
                print("Dealer WINS!\n")
                playAgain()
            elif dealerTotal < 21 and dealerTotal < playerTotal:
                print("Player WINS!\n")
                playAgain()
            elif dealerTotal == playerTotal:
                print("PUSH\n")
                playAgain()

def hitOrStand():
    hitOrStand = int(input("1 - Hit Me\n2 - Stand\n----> "))
    if hitOrStand == 1:
        hit()
    else:
        stand()

def game(): 
    global dealerHand
    global playerHand
    global dealerTotal
    global playerTotal

    print("Black Jack by Santiago Gorza")

    drawCardDealer()
    drawCardPlayer()
    drawCardPlayer()
    if playerHand == [10, "A"] or playerHand == ["A", 10]:
        print("Player has BLACKJACK!")
        playAgain()

    print("Dealer: ", dealerHand, "Count: ", dealerTotal)
    print("Player: ", playerHand, "Count: ", playerTotal,"\n")

    hitOrStand()

    while playerTotal < 21:
        hitOrStand()
       
    if playerTotal == 21:
        stand()
    elif playerTotal > 21:
        print("Player BUSTED!\n")
        playAgain()

            
def playAgain():
    global dealerHand
    global playerHand
    global dealerTotal
    global playerTotal
    global deck
    playAgain = int(input("Play again?\n1 - Yes\n2 - No\n--->"))
    if playAgain == 1:
        dealerHand = []
        playerHand = []
        dealerTotal = 0
        playerTotal = 0
        deck = 4 * ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A])
        game() 
    else:
        sys.exit("SUCK A DICK BITCHES!")

game()
