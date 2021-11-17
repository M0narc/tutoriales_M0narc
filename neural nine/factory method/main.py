from abc import ABCMeta, abstractstaticmethod


# the I before Person indicates that this is an interface
# abstract classes can't be instantiated
class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """interface method"""


class Student(IPerson):

    def __init__(self):
        self.name = "Basic student"

    def person_method(self):
        print("I'm a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "basic teacher"

    def person_method(self):
        print("I'm a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        try:
            if person_type == "Student":
                return Student()
            elif person_type == "Teacher":
                return Teacher()
        except TypeError:
            "No such person type"

    def __str__(self):
        """
        Factory method es un patrón de diseño creacional que resuelve el problema de crear objetos de
        producto sin especificar sus clases concretas.
        Identificación: Los métodos fábrica pueden ser reconocidos por métodos de creación, que crean objetos de
        clases concretas, pero los devuelven como objetos del tipo abstracto o interfaz.
        """
        return "read the text INSIDE __str__"


if __name__ == "__main__":
    choice = input("What type of person do you want to create? \n")
    person = PersonFactory.build_person(choice)
    person.person_method()
