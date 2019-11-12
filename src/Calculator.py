
def addition(a,b):
    return a+b

class Calculator:
    result=0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result= addition(a,b)
        return self.result


