class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        alive_animal = f'{{Name: {self.name}, Health: {self.health},' \
                       f' Hidden: {self.hidden}}}'
        return alive_animal


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = self.hidden
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore):
        if herbivore.hidden or isinstance(herbivore, Carnivore):
            herbivore.health = herbivore.health
        else:
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
