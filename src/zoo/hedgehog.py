
# elephant.py

from .animal import Animal


class HedgeHog(Animal):
    def __init__(self, name="Ellie"):
        super().__init__(name, species="HedgeHog")

    def sound(self):
        return "snuffles"

    def action(self):
        return "spikes people"
