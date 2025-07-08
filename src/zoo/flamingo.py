
# flamingo.py

from .animal import Animal


class Flamingo(Animal):
    def __init__(self, name="Flora"):
        super().__init__(name, species="Flamingo")

    def sound(self):
        return "honks"

    def action(self):
        return "balances gracefully on one leg!"
