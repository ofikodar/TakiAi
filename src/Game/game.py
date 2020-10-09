from src.Game.deck import Deck
from src.Game.player import Player


class Game:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
        self.turn = Turn(num_players)
        self.last_card = None

        self._create_players()
        self._init_game()

    def _create_players(self):
        for player_num in range(self.num_players):
            new_player = Player(name=str(player_num))
            self.players.append(new_player)

    def _init_game(self):
        for player in self.players:
            player.create_hand(self.deck)
        self.last_card = self.deck.get_first_card()
        print("last card:", self.last_card)

    def _check_win(self, player):
        return player.hand_size == 0

    def start(self):
        index = 0
        while True:
            current_player = self.players[index]
            current_player.play(self.last_card, self.deck)
            if self._check_win(current_player):
                print(f"player {current_player.name} wins..")
                exit()


class Turn:
    def __init__(self, num_players):
        self.num_players = num_players
        self.player_index = 0
        self.turn_direction = 1  # -1 for left, 1 for right

    def whose_turn(self, last_card):
        if last_card.name == 'stop':
            self._update_index()
            self._update_index()
        elif last_card.name == 'change direction':
            self.turn_direction *= -1
            self._update_index()

        else:
            self._update_index()
        return self.player_index

    def _update_index(self):
        self.player_index = self.player_index + self.turn_direction
        if self.player_index < 0:
            self.player_index = self.num_players - 1
        if self.num_players <= self.player_index:
            self.player_index = 0


if __name__ == '__main__':
    game = Game(num_players=4)
    game.start()
