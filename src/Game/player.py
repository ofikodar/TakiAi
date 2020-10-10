import random

from src.Game.deck import CARD_COLORS

INITIAL_NUM_CARDS = 8


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return f'player name: {self.name} , player hand:{str(self.hand)}'

    def create_hand(self, deck):
        self.hand.init_hand(deck)
        self.hand_size = len(self.hand)

    def play(self, last_card, deck, take_two_acc):
        """if player can play, not stopped
        last card can be stop form the player before 2 turns.
        let the player always play random optional card or only to pull
        """
        optional_cards = self.hand.get_optional_cards(last_card)
        to_pull = len(optional_cards) == 0
        if to_pull:
            pull_num = 1
            if last_card.name == 'take two' and not last_card.used:
                last_card.used = True
                pull_num = take_two_acc
            for _ in range(pull_num):
                print("* pulling from deck")
                self.hand.pull_from_deck(deck)
                self.hand_size += 1
            take_two_acc = 0
        else:
            card = random.choice(optional_cards)
            self.hand.play_card(card)
            self.hand_size -= 1
            print("* playing:", str(card))

            if card.name == 'take two' and not card.used:
                take_two_acc += 2
            if card.name == 'king' and not card.used:
                take_two_acc = 0

            if card.name == 'change color':
                card.color = random.choice(CARD_COLORS)
            if card.name == 'super taki':
                card.color = last_card.color if last_card.color is not None else random.choice(CARD_COLORS)
                print("* super taki color:", card.color)

            if 'taki' in card.name:
                taki_on = True
                optional_cards = self.hand.get_optional_cards(card, taki_on)
                while len(optional_cards) != 0 and card.name != 'change color' and self.hand_size != 0:
                    card = random.choice(optional_cards)
                    self.hand.play_card(card)
                    self.hand_size -= 1
                    print("* playing:", str(card))
                    optional_cards = self.hand.get_optional_cards(card)

            last_card = card

        return last_card, take_two_acc


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

    def get_optional_cards(self, last_card, taki_on=False):
        return [card for card in self.hand if card.is_playable(last_card,taki_on)]
