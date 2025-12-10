# A -- 23,34,56

# B -- Addition  -- showAddition()

# C -- Multiplication-- ShowMulti() 

# D -- showAll() -- 

class A:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def addition(self):
        print(f"{self.a + self.b +  self.c}")

class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def multiplication(self):
        print(f"{self.a * self.b * self.c}")
        
class D(C):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def showAll(self):
        self.addition()
        self.multiplication()

obj = D(10,20,30)
obj.showAll()




