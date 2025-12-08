# get student data and print data using class and object

# class student:

#     def get_data(self):# self is keyword and it represents the current  object of class
#         self.name ="John"
#         self.age = 23
#         self.marks = 34

#     def show_data(self):
#         return f" Name :- {self.name}\n Age :- {self.age} \n Marks :- {self.marks}"

# obj = student()
# obj.get_data()
# print(obj.show_data())

# Print Student Marksheet -- sname,m1,m2,m3,total ,percentage, as per per grade -- 
# >=70 - "A"
# 60-70 - "B"
# 50 -40 -- "C"
# Fail


class student:
    def get_data(self,rno,name,m1,m2,m3):
        self.rno = rno
        self.name = name 
        self.m1 = m1 
        self.m2 = m2 
        self.m3 = m3
    def show_data(self):
        self.total = self.m1 + self.m2 + self.m3 
        self.per = (self.total/3)*100
        if self.per >=70:
            self.grade= "A"
        elif self.per>=60 and self.per<70:
            self.grade ="B"
        elif self.per>=50 and self.per<60:
            self.grade ="C"
        else:
            self.grade="Fail"
        print(f"Name :-{self.name}\n M1:-{self.m1} \n ")


obj = student() 
obj.get_data(1,"ABC",89,78,67)



    
# Constructor -- It is useful for to initialize the objects . constructor is a special type of method .It invoked automatically when creating the object .
    
#     How to define constructor in python -
 
#     __init__ method

    #  __del__method