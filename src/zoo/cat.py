
# elephant.py

from .animal import Animal


class Cat(Animal):
    def __init__(self, name="Ca"):
        super().__init__(name, species="Cat")

    def sound(self):
        return "meows"

    def action(self):
        return "rules!"
