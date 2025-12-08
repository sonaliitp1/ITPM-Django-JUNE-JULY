class Person:
    
    def __init__(self,a):  # Parametrised Constructor
        self.a = a

        print(f"Object value :-{self.a}")
    
    # def __init__(self):  # default constructor
       #     print("Constructor Calling.....")
 
obj = Person(200)
obj1 = Person(300)
obj2 = Person(400) 



