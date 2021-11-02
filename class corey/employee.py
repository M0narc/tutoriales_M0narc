
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


print(Employee.__dict__)
