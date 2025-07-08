
# Camel.py

from .animal import Animal


class Camel(Animal):
    def __init__(self, name="Ellie"):
        super().__init__(name, species="Camel")

    def sound(self):
        return "AaAaOoOo"

    def action(self):
        return "Adapt to arid environments "
        
