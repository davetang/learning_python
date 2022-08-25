#!/usr/bin/env python3
#
# class adapted from https://www.tutorialspoint.com/python/python_classes_objects.htm
#
# https://realpython.com/python-super/ provides nice use cases of super()
#
# super() gives you access to methods in a superclass from the subclass that
# inherits from it. super() alone returns a temporary object of the superclass
# that then allows you to call that superclass’s methods. A common use case of
# super() is building classes that extend the functionality of previously built
# classes. Calling the previously built methods with super() saves you from
# needing to rewrite those methods in your subclass, and allows you to swap out
# superclasses with minimal code changes.
#
# The SO post below has more technical points regarding the difference between
# using super().__init__ versus Employee.__init__:
#
# https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
#

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def emp_num(self):
        print("Employee number: {}".format(Employee.emp_count))

    def emp_display(self):
        print("Name: {}\nSalary: {}".format(self.name, self.salary))

    def raise_salary(self, perc):
        self.salary = round(self.salary + self.salary * perc / 100, 2)

homer = Employee("Homer Simpson", 24395.80)
homer.emp_display()
homer.raise_salary(1)
homer.emp_display()

class Boss(Employee):
    def __init__(self, name, salary):
        # super takes two parameters: the subclass and an object
        # in Python 3, super(Boss, self) is equivalent to super()
        # this will look for methods one level above Boss
        # if there are more levels, a higher subclass can be specified
        # however, the parameterless call to super() is recommended and
        # sufficient in more use cases
        super().__init__(name, salary)
        # See https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
        # on why the code below is not recommended
        # Employee.__init__(self, name, salary)

    # override
    def raise_salary(self, amount):
        self.salary = round(self.salary + amount, 2)

monty = Boss("Montgomery Burns", 1000000)
monty.emp_display()
monty.raise_salary(1000000)
monty.emp_display()

monty.emp_num()

