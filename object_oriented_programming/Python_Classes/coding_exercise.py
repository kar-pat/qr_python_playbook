"""
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

How can you achieve this with only 2 methods?

How can you make sure you only have one instance of each playing card?

How can you make your playing card instances print in a nice format?

Add a class to represent a deck of cards - how can you integrate these two classes together?
"""
