from src.Game.cards import RegularCard, StrongCard, SuperCard

CARD_COLORS = ['red', 'yellow', 'blue', 'green']
STRONG_CARDS_NAMES = ['stop', 'taki', 'add', 'takeTwo']
SUPER_CARDS_NAMES = ['change', 'super', 'king']


class Deck:
    def __init__(self):
        self.deck = []
        self._create_regulars()
        self._create_strong()
        self._create_super()

    def _create_regulars(self):
        regulars = [RegularCard(number, color) for color in CARD_COLORS for number in range(1, 10)] * 2
        self.deck += regulars

    def _create_strong(self):
        strong = [StrongCard(name, color) for color in CARD_COLORS for name in STRONG_CARDS_NAMES] * 2
        self.deck += strong

    def _create_super(self):
        super = [SuperCard(name) for name in SUPER_CARDS_NAMES] * 2
        super += [SuperCard(SUPER_CARDS_NAMES[0])] * 2
        self.deck += super


if __name__ == '__main__':
    Deck()
