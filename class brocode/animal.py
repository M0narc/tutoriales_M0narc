class Organism:
    alive = True


class Animal(Organism):

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Animal, Prey):

    def run(self):
        print("This rabbit is running")

    def eat(self):
        print("This rabbit is eating a carrot")


class Fish(Animal, Predator):

    def swim(self):
        print("This fish is swimming")

    def eat(self):
        print("This fish is eating sediment")


class Hawk(Animal, Prey, Predator):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
