# chinchilla.py

from .animal import Animal


class Chinchilla(Animal):
    def __init__(self, name="Chinny"):
        super().__init__(name, species="Chinchilla")

    def sound(self):
        return "squeaks"

    def action(self):
        return "floofs up"