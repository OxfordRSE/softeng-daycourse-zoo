# pterodactyl.py

from .animal import Animal


class Pterodactyl(Animal):
    def __init__(self, name="Tilly"):
        super().__init__(name, species="Pterodactyl")

    def sound(self):
        return "shrieks"

    def action(self):
        return "swooshes around soulfully."
