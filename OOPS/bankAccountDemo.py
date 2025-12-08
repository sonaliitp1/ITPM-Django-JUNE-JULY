class Bank:
    def __init__(self,accno,acctname,initialbal,depositbal,withbal):
        self.accno = accno
        self.acctname = acctname
        self.initialbal = initialbal
        self.depositbal = depositbal
        self.withbal = withbal

    def deposittAmt(self):
        self.dbal =self.initialbal + self.depositbal

    def withAmt(self):
        if(self.dbal>self.withbal):
            self.fbal = self.dbal - self.withbal
        else:
            print("Insufficient Amount....")

    def showinf(self):
        print(f"{self.accno} \t {self.acctname} \t {self.initialbal} \t {self.depositbal} \t {self.withbal} \t {self.fbal}")

obj = Bank(1001,"ABC",10000,4000,3000)
obj.deposittAmt()
obj.withAmt()
obj.showinf()