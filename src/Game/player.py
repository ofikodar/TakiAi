INITIAL_NUM_CARDS = 8


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return f'player name: {self.name} , player hand:{str(self.hand)}'

    def create_hand(self, deck):
        self.hand.init_hand(deck)

    def play(self, last_card):
        """if player can play, not stopped
        last card can be stop form the player before 2 turns"""
        print(self.hand)
        optional_cards = self.hand.get_optional_cards(last_card)
        [print(card) for card in optional_cards]


class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand_str = '========== hand =========== \n'
        for card in self.hand:
            hand_str += str(card) + '\n'
        hand_str += '--------------------------'
        return hand_str

    def init_hand(self, deck):
        for _ in range(INITIAL_NUM_CARDS):
            card = deck.pull()
            self.hand.append(card)

    def get_optional_cards(self, last_card):
        return [card for card in self.hand if card.is_playable(last_card)]

