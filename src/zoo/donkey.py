
# donkey.py

from .animal import Animal


class Donkey(Animal):
    def __init__(self, name="Hija"):
        super().__init__(name, species="Donkey")

    def sound(self):
        return "ia"

    def action(self):
        return "does what it wants!"