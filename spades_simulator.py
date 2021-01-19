# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:41:00 2020

@author: stuar
"""
#TODO: Write function to deal cards to each player
import random
random.seed(0)
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def set_suit(self, suit):
        self.suit = suit
    def set_value(self, value):
        self.value = value
    def __str__(self):
        if self.value == 11:
            return "The Jack of " + str(self.suit) + 's'
        elif self.value == 12:
            return "The Queen of " + str(self.suit) + 's'
        elif self.value == 13:
            return "The King of " + str(self.suit) + 's'
        elif self.value == 14:
            return "The Ace of " + str(self.suit) + 's'
        elif self.value == 15:
            return "The Little"
        elif self.value == 16:
            return "The Big"
        else:
            return "The " + str(self.value) + " of " + str(self.suit) + 's'

    
def gen_deck(spades_deck = False):
    suits = ["Diamond", "Heart", "Club", "Spade"] #13
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    deck_of_cards = []
    for i in range(4):
        for n in range(13):
            deck_of_cards.append(Card(suits[i],values[n]))
    if spades_deck == True:
        deck_of_cards[0] = Card('Spade',15)
        deck_of_cards[13] = Card('Spade',16)
    return(deck_of_cards)      
        
def deal():
    all_hands = [[],[],[],[]]
    deck = gen_deck(spades_deck = True)
    while True:
        for hand in all_hands:
            card_dealt = deck.pop(random.randint(0, len(deck)-1))
            hand.append(card_dealt)
        if len(deck) == 0:
            break
    return all_hands

def analyse_hand(hand):
    spade_value = 0
    predicted_books = 0
    all_suits = [0,0,0,0] #clubs, diamonds, hearts, spades
    for card in hand:
        if card.get_suit() == 'Spade':
            spade_value += card.get_value()
        if card.get_value() == 14 and card.get_suit() != "Spade":
            predicted_books += 1
        if card.get_value() == 16:
            predicted_books += 1
        if card.get_suit() == "Club":
            all_suits[0] += 1
        if card.get_suit() == "Diamond":
            all_suits[1] += 1
        if card.get_suit() == "Heart":
            all_suits[2] += 1
        if card.get_suit() =="Spade":
            all_suits[3] += 1
    if all_suits[0] == 0 or all_suits[1] == 0 or all_suits[2] == 0:
        predicted_books += 1
    predicted_books += round(spade_value/16)
    return predicted_books
    

def analyse_all_hands(all_hands): #do the analysis of 9 and 8 book hands here
    list_of_hands = []
    for hand in all_hands:
        books_predicted = analyse_hand(hand)
        if books_predicted == 9:
            for card in hand:
                print(card)
            print('-------------------------------------------------------------')
        list_of_hands.append(books_predicted)
    return (list_of_hands)



def test_model():
   
    all_hands = deal()
    list_of_books = analyse_all_hands(all_hands)
    total_books = 0
    bet3 = 0
    bet4 = 0
    bet5 = 0
    for book in list_of_books:
        total_books += book
        if book == 3:
            bet3 += 1
        if book == 4:
            bet4 += 1
        if book ==5:
            bet5 += 1
    return (total_books, bet3, bet4, bet5)
    


def monte_carlo(trials):
    expected_books = 13
    book_total = 0
    bet3total = 0
    bet4total = 0
    bet5total = 0
    for i in range(trials):
        actual_books, bet3, bet4, bet5 = test_model()
        book_total += actual_books
        bet3total += bet3
        bet4total += bet4
        bet5total += bet5
    threepcent = ((bet3total/4)*100)/trials
    fourpcent = ((bet4total/4)*100)/trials
    fivepcent = ((bet5total/4)*100)/trials

    n = expected_books*trials
    print( "Across " + str(trials) + " trials: ")
    print("The percentage that betting 3 was correct = " + str(threepcent)+ "%")
    print("The percentage that betting 4 was correct = " + str(fourpcent)+ "%")
    print("The percentage that betting 5 was correct = " + str(fivepcent) + "%")
    print("The percentage that the model was correct = " +  str((book_total / n)*100) + "%" )
    return
    

monte_carlo(10000)










