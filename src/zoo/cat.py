# cat.py

from .animal import Animal


class Elephant(Animal):
    def __init__(self, name="Tommy"):
        super().__init__(name, species="Cat")

    def sound(self):
        return "meow"

    def action(self):
        return "eats fish"