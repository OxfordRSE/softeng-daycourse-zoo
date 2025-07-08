
# elephant.py

from .animal import Animal


class RedPanda(Animal):
    def __init__(self, name="Tashi"):
        super().__init__(name, species="Red Panda")

    def sound(self):
        return "squeals, twitters, huff quacks, hisses and grunts"

    def action(self):
        return "plays in trees!"
