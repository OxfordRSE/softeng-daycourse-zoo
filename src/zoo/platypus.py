from .animal import Animal 

class Platypus(Animal):
    def __init__(self, name = "Perry"):
        super().__init__(name, species="Platypus")
    
    def sound (self):
        return "quacks"

    def action (self):
        return "fights crime."
        # kangaroo.py


