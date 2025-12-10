class A:
    def __init__(self,a,b):
        self.num1 = a 
        self.num2 = b 
    
    def calculate(self):
        print(f"{self.num1 + self. num2}")

class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)

    def show(self):
        mul = self.num1 * self.num2
        print(mul)
        self.calculate()
     
    
obj = B(23,34)
obj.show()