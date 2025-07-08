
# elephant.py

from .animal import Animal


class Dog(Animal):
    def __init__(self, name="Henry"):
        super().__init__(name, species="Dog")

    def sound(self):
        return "barks"

    def action(self):
        return "Friendly!"
