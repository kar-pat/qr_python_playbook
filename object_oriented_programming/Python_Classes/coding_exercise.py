
'''
Write a class that represents playing cards.

Augment your class definition so that instances can be compared with the
inequality operators, `>, <, ==, !=, <=, >=`. The cards are ordered such that
Clubs > Hearts > Spades > Diamonds, Ace is high, with the value taking precedence
over suit.

>>> ace_spades > ace_hearts
False
>>> queen_diamonds > three_clubs
True
>>> five_hearts <= ace_hearts
True

How can you achieve this with only 2 methods? ????

How can you make sure you only have one instance of each playing card? Done.

How can you make your playing card instances print in a nice format? Done. 
Add a class to represent a deck of cards - how can you integrate these two classes together?
'''

import random

class Card(object):

    suit_dictionary = {"DIAMONDS": 1, "SPADES": 2, "HEARTS": 3, "CLUBS": 4}
    value_dictionary = {'ACE':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'JACK':11, 'QUEEN':12, 'KING':13}
    cards_list = {'SPADES': [], 'HEARTS': [], 'DIAMONDS': [], 'CLUBS': []}


    def __init__(self, suit, value):
        if suit.upper() not in self.suit_dictionary.keys() or str(value).upper() not in self.value_dictionary.keys():
            raise ValueError("Invalid suit or value")
        elif str(value).upper() in self.cards_list[suit.upper()]:
            raise ValueError("Card already exists")
        else:
            self.suit = suit.upper()
            self.value = str(value).upper()
            self.cards_list[self.suit].append(self.value)
            self._suit_rank = self.suit_dictionary[self.suit]
            self._value_rank = self.value_dictionary[self.value]

    def card_deck(self, suit, value):
        
        self.suit = suit.upper()
        self.value = str(value).upper()
        self._suit_rank = self.suit_dictionary[self.suit]
        self._value_rank = self.value_dictionary[self.value]


    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    
    def __gt__(self, other):
        if self._value_rank > other._value_rank:
            return True
        elif self._value_rank == other._value_rank:
            if self._suit_rank > other._suit_rank:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self._value_rank < other._value_rank:
            return True
        elif self._value_rank == other._value_rank:
            if self._suit_rank < other._suit_rank:
                return True
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if self._value_rank == other._value_rank:
            if self._suit_rank == other._suit_rank:
                return True
            else:
                return False
        else:
            return False
    
    def __ne__(self, other):
        if self._value_rank != other._value_rank and self._suit_rank != other._suit_rank:
            return True
        else:
            return False

    def __le__(self, other):
        if self._value_rank <= other._value_rank:
            return True
        elif self._value_rank == other._value_rank:
            if self._suit_rank <= other._suit_rank:
                return True
            else:
                return False
        else:
            return False
    
    def __ge__(self, other):
        if self._value_rank >= other._value_rank:
            return True
        elif self._value_rank == other._value_rank:
            if self._suit_rank >= other._suit_rank:
                return True
            else:
                return False
        else:
            return False
    

class Deck():
    
    suit_dictionary = {"DIAMONDS": 1, "SPADES": 2, "HEARTS": 3, "CLUBS": 4}
    value_dictionary = {'ACE':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'JACK':11, 'QUEEN':12, 'KING':13}

    def __init__(self):
        self.cards = []
        self.assemble_deck()

    def assemble_deck(self):    
        for suit in Deck.suit_dictionary:
            for value in Deck.value_dictionary:
                self.cards.append(Card.card_deck(self, suit, value))
    
    def __str__(self):
        return f"{self.cards}"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


x = Card("Diamonds", "Ace")
z = Card("Diamonds", "4")
y = Card("Hearts", "Queen")
deck1 = Deck()
print(x)
print(z)
print(y)
print(x > y)
print(Card.cards_list)
print(deck1)