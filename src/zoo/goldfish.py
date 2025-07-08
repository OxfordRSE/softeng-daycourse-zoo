
# goldfish.py

from .animal import Animal


class Goldfish(Animal):
    def __init__(self, name="Goldie"):
        super().__init__(name, species="Goldfish")

    def sound(self):
        return "blub"

    def action(self):
        return "Just keeps swimming"
