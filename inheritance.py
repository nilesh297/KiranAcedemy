# inheritance :
# chiled class/derived class aquire all methods and variable in parent class/super class/ base class
# syntax: 
    #class P1:
        # pass
    # class c1(P1):
        # pass

# class P1:
#     def hello(self):
#         print("i am parent class")
# class C1(P1):
#     def hello1(self):
#         print("i am child class")

# p1 = P1()   # parent class
# p1.hello()

# c1= C1()
# c1.hello1()
# c1.hello()

# Example 2
class P1:
    class1="the kiran acedemy"
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(f"my name is {self.fname} {self.lname}")

class C1(P1):
    def __init__(self, fname, lname, age, address):
        super().__init__(fname, lname)
        self.age= age
        self.address= address
        
        def display1(self):
            print(f"my name is {self.fname} {self.lname} and my age is {self.age} I live in {self.address}")

