
# raccoon.py

from .animal import Animal


class Elephant(Animal):
    def __init__(self, name="Rocky"):
        super().__init__(name, species="Raccoon")

    def sound(self):
        return "screeches"

    def action(self):
        return "dumpster dives!"
