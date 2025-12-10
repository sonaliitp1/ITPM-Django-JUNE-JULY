class Bank:
    def __init__(self,bankname,balance):
        self.bname = bankname
        self.bal = balance

class SavingAccount(Bank):
    def __init__(self, bankname, balance):
        super().__init__(bankname, balance) 
    
    def calculate_savingInt(self):
        self.savingbal = self.bal + self.bal * 0.03 
        
class CurrentAccount(Bank):
    def __init__(self, bankname, balance):
        super().__init__(bankname, balance)
    
    def calculate_currentInt(self):
        self.currentbal = self.bal + self.bal * 0.04

class Customer(SavingAccount,CurrentAccount):
    def __init__(self, bankname, balance,cname,acctno):
        super().__init__(bankname, balance)
        self.cname = cname
        self.acctno = acctno
    def show_details(self):
        self.calculate_savingInt()
        self.calculate_currentInt()
        print(f"{self.bname} \t {self.acctno} \t {self.cname} \t {self.savingbal} \t {self.currentbal}")
    
obj = Customer("Bank Of India",567899,"Rohit",1122)
obj.show_details()



 
 