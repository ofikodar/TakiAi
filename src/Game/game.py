from src.Game.deck import Deck
from src.Game.player import Player


class Game:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
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

    def turn(self, player_index):
        current_player = self.players[player_index]
        current_player.play(self.last_card)


if __name__ == '__main__':
    game = Game()
    game.turn(0)