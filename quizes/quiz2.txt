1. What is the output of the program

class A:
    def __getInfo(self):
        return "A's getInfo is called"

    def printInfo(self):
        print(self.__getInfo(), end = ' ')

class B(A):
    def __getInfo(self):
        return "B's getInfo is called"

def main():
    A().printInfo()
    B().printInfo()

main()

a) A’s getInfo is called A’s getInfo is called
b) A’s getInfo is called B’s getInfo is called
c) B’s getInfo is called A’s getInfo is called
d) B’s getInfo is called B’s getInfo is called

2. What is the output of the below program?

class A:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y

    def __str__(self):
        return "A"

    def __eq__(self, num ):
        return self.x * self.y == num.x * num.y



def main():
    a = A(1, 2)
    b = A(2, 1)
    print(a == b)

main()

a) True
b) False
c) 2
d) 1

3.What is the output of the following program

class A:
    def __init__(self):
        return "A"

class B(A):
    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()

def main():
    b = B()
    a = A()
    c = C()
    print(a, b, c)

main()

a) B B B
b) A B C
c) C B A
d) A A A

4. What is the output of the following program

class A:
    def __init__(self):
        self.x = 1

    def func(self):
        self.x = 10

class B(A):
    def func(self):
        self.x += 1
        return self.x

def main():
    b = B()
    print(b.func())

main()

a) 1
b) 2
c) 10
d) x is not accessible from the object of class B

5. What is the output of the following program

class A:
    def __init__(self, num):
        self.x = num

class B(A):
    def __init__(self, num):
        self.y = num

obj = B(11)
print ("%d %d" % (obj.x, obj.y))

a) None None
b) None 11
c) 11 None
d) 11 11
e) Attribute Error: 'B' object has no Attribute 'x'


6. What will be the output of the following program
class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")

class B(A):
    def __new__(self):
        print("B's __new__() invoked")

    def __init__(self):
        print("B's __init__() invoked")

def main():
    b = B()
    a = A()

main()

a) B's __new__() invoked A's __init__() invoked
b) B’s __new__() invoked A’s __new__() invoked
c) B’s __new__() invoked A’s __init__() invoked A’s __new__() invoked
d) A’s __init__() invoked A’s __new__() invoked

7. What is the output of the following program ?

class A:
    def __init__(self, x = 0):
        self.x = x

    def func1(self):
        self.x += 1

class B(A):
    def __init__(self, y = 0):
       A.__init__(self, 3)
        self.y = y

    def func1(self):
        self.y += 1

def main():
    b = B()
    b.func1()
    print(b.x, b.y)

main()

a) 2 0
b) 3 1
c) 4 0
d) 3 0
e) 4 1

8. What is the output of the following program
class A:
     def __init__(self):
         self.__x = 1
         self.y = 10

     def printclass(self):
         print(self.__x, self.y)

class B(A):
     def __init__(self):
         super().__init__()
         self.__x = 2
         self.y = 20

c = B()
c.printclass()

a) 1 10
b) 1 20
c) 2 10
d) 2 20

9. What is the output of the following program
class A:
    def __init__(self, x = 1):
        self.x = x

class B(A):
    def __init__(self, y = 2):
        super().__init__()
        self.y = y

def main():
    b = B()
    print(b.x, b.y)

main()

a) 0 0
b) 0 1
c) 1 2
d) 0 2
e) 2 1

10. What is the output of the following program

class Counter:
    def __init__(self):
        self.counter = 0

def main():
    myCounter = Counter()
    num = 0

    for i in range(0, 100):
        increment(myCounter, num)

    print("myCounter.counter =", myCounter.counter, ", number of times =", num)

def increment(c, num):
    c.counter += 1
    num += 1

main()

a) counter is 101, number of times is 0
b) counter is 100, number of times is 0
c) counter is 100, number of times is 100
d) counter is 101, number of times is 101
