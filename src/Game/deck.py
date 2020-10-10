import random

from src.Game.cards import Card

CARD_COLORS = ['red', 'yellow', 'blue', 'green']
STRONG_CARDS_NAMES = ['change direction', 'stop', 'taki', 'add one', 'take two']
SUPER_CARDS_NAMES = ['change color', 'super taki', 'king']


class Deck:
    def __init__(self):
        self.deck = []
        self._create_cards()

    def __str__(self):
        return ' ,'.join(self.deck)

    def pull(self):
        if len(self.deck) == 0:
            self._create_cards()
            print("finished deck")
        card = self.deck[0]
        del self.deck[0]
        return card

    def get_first_card(self):
        for i, card in enumerate(self.deck):
            if card.type == 'regular':
                del self.deck[i]
                return card

    def _create_cards(self):
        self._create_regulars()
        self._create_strong()
        self._create_super()
        random.shuffle(self.deck)

    def _create_regulars(self):
        regulars = [Card('regular', str(number), color) for color in CARD_COLORS for number in range(1, 10) for _ in
                    range(2)]
        self.deck += regulars

    def _create_strong(self):
        strong = [Card('strong', name, color) for color in CARD_COLORS for name in STRONG_CARDS_NAMES for _ in range(2)]
        self.deck += strong

    def _create_super(self):
        super = [Card('super', name) for name in SUPER_CARDS_NAMES for _ in range(2)]
        super += [Card('super', SUPER_CARDS_NAMES[0]) for _ in range(2)]
        self.deck += super
