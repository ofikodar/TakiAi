class Card:
    def __init__(self, type, name, color=None):
        self.name = name
        self.color = color
        self.type = type

    def __eq__(self, other):
        return other.name == self.name and other.color == self.color

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"

    def is_playable(self, last_card):
        """check can put my card on the last card"""
        if 'king' in [self.name, last_card.name]:
            return True
        if last_card.name == 'take two' and self.name != 'take two':
            return False
        if last_card.name == self.name or last_card.color == self.color:
            return True

        return False
