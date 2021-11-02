import datetime

from developer import Developer
from manager import Manager

if __name__ == "__main__":
    my_date = datetime.date.today()
    # print(Developer.is_workday(my_date))
    # print(Employee.__dict__)
    # help(Developer)
    dev0 = Developer("Fran", "Lujan", 20000, "_Python_")
    dev1 = Developer("Fran", "Matias", 20000, "Java")
    manage = Manager("Fran", "lujan", 8000, [dev0])
    manage.add_emp(dev1)
    print(dev0.last)
    print(dev1.last)
    print(manage.print_emp())
    manage.remove_emp(dev1)
    print(manage.print_emp())