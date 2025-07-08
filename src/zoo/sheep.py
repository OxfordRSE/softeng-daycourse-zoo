
# sheep.py

from .animal import Animal


class Sheep(Animal):
    def __init__(self, name="Carl"):
        super().__init__(name, species="Sheep")

    def sound(self):
        return "Silence, occasionally BAAAAAA"

    def action(self):
        return "A quiet, comforting presence"
