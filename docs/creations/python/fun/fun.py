#
# This program will: create a deck of cards that you can shuffle and draw from
#

import random as rand

class Deck():
    def __init__(self,decklist=list()):
        suits = ["Spades","Clubs","Hearts","Diamonds"]
        types = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        for suit in suits:
            for t in types:
                decklist.append("{} of {}".format(t,suit))
        self.deck = decklist
    def shuffle(self):
        orderlist = list(range(1,len(self.deck)))
        rand.shuffle(orderlist)
        shuffledeck = list()
        for i in orderlist:
            shuffledeck.append(self.deck[i])
        self.deck = shuffledeck
    def draw(self):
        return self.deck.pop(0)

class Hand():
    def __init__(self,handlist=list()):
        self.hand = handlist
    def drawcard(self,card_to_add)
        self.hand.append(card_to_add)
