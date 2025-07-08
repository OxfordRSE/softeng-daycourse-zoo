# wolf.py

from .animal import Animal


class Wolf(Animal):
    def __init__(self, name="Derek"):
        super().__init__(name, species="Wolf")

    def sound(self):
        return "howls"

    def action(self):
        return "Extremely loyal!"