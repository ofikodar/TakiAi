class RegularCard:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return f"number: {self.number}, color: {self.color}"


class StrongCard:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"


class SuperCard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name: {self.name}"
