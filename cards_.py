import random

suits = ('Hearts', 'Diamonds', 'Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit
        

class Deck():

    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                # This creates the Card object.
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        """ Now lets shuffle the new deck of cards """
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

class Player():

    def __init__(self,name):
        self.name = name
        # This is basically an empty hand
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):

        return f'Player1{self.name} has {len(self.all_cards)} cards'
        
        
            

    ## Player() class coming up which takes a name and allows for creation of player objects later on



    
