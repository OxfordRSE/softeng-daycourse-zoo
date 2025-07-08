
# elephant.py

from .animal import Animal


class Et(Animal):
    def __init__(self, name="Egg"):
        super().__init__(name, species="Alien")

    def sound(self):
        return "zuzi"

    def action(self):
        return "can not lie"
