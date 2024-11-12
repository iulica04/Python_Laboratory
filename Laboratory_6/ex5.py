#Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish. Add properties and methods to represent
# characteristics unique to each animal group.



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def move(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return f"{self.name} makes a mammalian sound."

    def move(self):
        return f"{self.name} is walking."

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return f"{self.name} chirps."

    def move(self):
        return f"{self.name} is flying."

class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return f"{self.name} makes a bubbling sound."

    def move(self):
        return f"{self.name} is swimming."


if __name__ == '__main__':
    mammal = Mammal("Lion", "Panthera leo")
    print(mammal.make_sound())
    print(mammal.move())

    bird = Bird("Eagle", "Aquila chrysaetos")
    print(bird.make_sound())
    print(bird.move())

    fish = Fish("Goldfish", "Carassius auratus")
    print(fish.make_sound())
    print(fish.move())
