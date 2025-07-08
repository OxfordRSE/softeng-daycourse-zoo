# hedgehog.py

from .animal import Animal


class hedgehog(Animal):
    def __init__(self, name="Derek"):
        super().__init__(name, species="Hedgehog")

    def sound(self):
        return "squeeks"

    def action(self):
        return "Pricks things with its spikes"