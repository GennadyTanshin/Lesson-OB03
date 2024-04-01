class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} говорит "

    def eat(self):
        return f"{self.name} ест."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} говорит Чирик!"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} говорит Гав!"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} говорит Ш-ш-ш!"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())



class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Зоозащитник кормит {animal.name}")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен {type(staff_member).__name__} в сотрудники зоопарка")



bird = Bird("Воробей", 2)
mammal = Mammal("Собака", 5)
reptile = Reptile("Змеюка", 4)

animals = [bird, mammal, reptile]

animal_sound(animals)

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper()
vet = Veterinarian()

zoo.add_staff(keeper)
zoo.add_staff(vet)

keeper.feed_animal(mammal)
vet.heal_animal(reptile)