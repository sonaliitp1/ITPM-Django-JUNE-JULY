class A:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    
    def addition(self):
        print(f"{self.a + self.b}")
        
class B:
    def __init__(self,c,d):
        self.c = c 
        self.d = d 
    def multi(self):
        print(f"{self.c * self.d}")

class C(A,B):
    def __init__(self, a, b,c,d):
        A.__init__(self,a, b)
        B.__init__(self,c,d)
    
    def showAll(self):
        self.addition()
        self.multi()

obj = C(10,20,30,40)
obj.showAll()

'''
single Inheritance - 

Account  -- Acct_no,Acct_name,balance,acct_type- saving , current

BankAccount --- intrest - showAllDetails() --all information including intreset 3 %

3,4

'''