from abc import ABCMeta, abstractstaticmethod


# the I before Person indicates that this is an interface
# abstract classes can't be instantiated
class IPerson(meta=ABCMeta):

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

    def build_person(self):
        pass
