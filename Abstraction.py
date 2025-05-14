# Abstraction:
    # Hide Internal data from user show only neccessary data
    # Achive using abstract class and interface



# Interface Example
from abc import ABC , abstractmethod
class Parent(ABC):
    @abstractmethod
    def Addition(self):
        num1= 20
        num2= 30
        add= num1 + num2
        print(add)
    def _Abstract_method(self):
        print("abstract method")
class Child(Parent):
    def Addition(self):
        return super().Addition()
    def _Abstract_method(self):
        return super()._Abstract_method()
c= Child()
c.Addition()