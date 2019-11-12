import math

def addition(a,b):
    return a+b

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a,b):
    return a*b

def division(a,b):
    c=b/a
    return round(c,9)

def square(a):
    d = a**2
    return d

def square_root(a):
    c=math.sqrt(a)
    return round(c,8)

class Calculator:
    result=0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result= addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result= subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result= multiplication(a,b)
        return self.result

    def divide(self, a, b):
        self.result= division(a,b)
        return self.result

    def doubled(self, a):
        self.result = square(a)
        return self.result

    def sq_root(self, a):
        self.result = square_root(a)
        return self.result
    