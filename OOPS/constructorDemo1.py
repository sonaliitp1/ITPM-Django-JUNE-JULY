class Employee:

    companyName ="ITP"

    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename 
        self.sal = sal
        print("Constructor Calling")
    
    def __del__(self):
        print("Destructor Calling")
    
    def showdata(self):
        print(f"{self.eid} and {self.ename} and {self.sal} and {Employee.companyName}")

       
    
obj = Employee(1,"ABC",45000)
obj1 = Employee(2,"XYZ",56000)
obj2 = Employee(3,"PQR",67000)
obj.showdata()
obj1.showdata()
obj2.showdata()


# take 3 employee Bank Account details -- acctname,acctno,balance,deposit amt,withdrawlamt

constructor, deposit(),withdrwal() , showinfo()