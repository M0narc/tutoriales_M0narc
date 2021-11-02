import datetime


# they allow us to logically group our data and functions
class Employee:
    # class variables can only be used by calling the class through Employee. or self.
    emp_num = 0
    raise_amount = 1.04

    # the init method is = to a constructor, that has attributes
    # the 'self' is the instance of the given obj, and it is and attribute
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.emp_num += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        # this CLASS method modify the class variable
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """
        from a string with dashes
        this is an alternative constructor
        :param emp_str: This param should have an input like
        this -> franco-lujan-7000
        :return:
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # regular methods automatically pass the instance as the first argument 'self'
    # static methods don't pass anything automatically
    # we include them in our classes cuz they have some logical connection
    # with the class, we can pass in the arguments that we want to work with

    @staticmethod
    def is_workday(day):
        """
        this method takes a date and returns a boolean
        :return:
        """
        if day.weekday() > 5:
            return False
        else:
            return True
