# hedgehog.py

from .animal import Animal


class Hedgehog(Animal):
    def __init__(self, name="Jack"):
        super().__init__(name, species="Hedgehog")

    def sound(self):
        return "snuffles"

    def action(self):
        return "spikes people"
