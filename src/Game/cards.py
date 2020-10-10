class Card:
    def __init__(self, type, name, color=None):
        self.name = name
        self.color = color
        self.type = type
        self.used = False

    def __eq__(self, other):
        return other.name == self.name and other.color == self.color

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"

    def is_playable(self, last_card, taki_color=None):
        """check can put my card on the last card"""

        if taki_color is not None :
            same_color = taki_color == self.color
            super_cards = self.type == 'super'
            if self.name == 'super taki':
                self.color = taki_color
            return  same_color or super_cards


        if 'king' in [self.name, last_card.name]:
            return True
        if self.name == 'super taki' and last_card.name != 'take two':
            return True
        if last_card.name == 'take two' and self.name != 'take two':
            return False
        if 'taki' in last_card.name and (self.color == last_card.color or self.color is None):
            return True


        if last_card.name == self.name or last_card.color == self.color:
            return True

        return False
