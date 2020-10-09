INITIAL_NUM_CARDS = 8


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.hand_size = len(self.hand)

    def __str__(self):
        return f'player name: {self.name} , player hand:{str(self.hand)}'

    def create_hand(self, deck):
        self.hand.init_hand(deck)

    def play(self, last_card, deck):
        """if player can play, not stopped
        last card can be stop form the player before 2 turns.
        let the player always play the first optional card or only to pull
        """
        optional_cards = self.hand.get_optional_cards(last_card)
        to_pull = len(optional_cards) == 0
        if to_pull:
            print("* pulling from deck")
            self.hand.pull_from_deck(deck)
            if last_card.name == 'take two':
                self.hand.pull_from_deck(deck)

        else:
            card = optional_cards[0]
            print("* playing:", str(card))
            self.hand.play_card(card)


class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand_str = '========== hand =========== \n'
        for card in self.hand:
            hand_str += str(card) + '\n'
        hand_str += '--------------------------'
        return hand_str

    def __len__(self):
        return len(self.hand)

    def init_hand(self, deck):
        for _ in range(INITIAL_NUM_CARDS):
            card = deck.pull()
            self.hand.append(card)

    def pull_from_deck(self, deck):
        card = deck.pull()
        self.hand.append(card)

    def play_card(self, play_card):
        for i, hand_card in enumerate(self.hand):
            if hand_card == play_card:
                del self.hand[i]
                return

    def get_optional_cards(self, last_card):
        return [card for card in self.hand if card.is_playable(last_card)]
