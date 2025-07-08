
# redpanda.py

from .animal import Animal


class Redpanda(Animal):
    def __init__(self, name="Charlie"):
        super().__init__(name, species="Redpanda")

    def sound(self):
        return "purrrr"

    def action(self):
        return "eternally sleeps!"
