from enum import Enum
from collections import deque
from random import shuffle
class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class Value(Enum):
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    suit = None
    value = None
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class BlackJackCard(Card):
    def __init__(self, suit, value):
        super().__init__(suit, value)
        self.value = min(value, 10)

class Hand:
    def __init__(self):
        self.cards = deque()

    def add_card(self, card):
        self.cards.append(card)
    
    def score(self):
        score = 0
        for card in self.cards:
            score += card.value
        return score

class BlackJackHand(Hand):
    def __init__(self):
        super().__init__()

    def score(self):
        minOver = float('inf')
        maxUnder = float('-inf')
        for score in self.possible_scores():
            if score > 21 and score < minOver:
                minOver = score
            elif score <= 21 and score > maxUnder:
                maxUnder = score
        return maxUnder if maxUnder != float('-inf') else minOver
    
    def possible_scores(self):
        score_no_aces = 0
        for card in self.cards:
            if card.value == Value.ACE:
                continue
            score_no_aces += card.value
        res = deque([score_no_aces])
        aces = [card for card in self.cards if card.value == Value.ACE]
        for ace in aces:
            sz = len(res)
            for i in range(sz):
                v = res.popleft()
                res.append(v + 1)
                res.append(v + 11)
        return res


class Deck:
    def __init__(self):
        self.cards = deque()
        for suit in Suit:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.popleft()