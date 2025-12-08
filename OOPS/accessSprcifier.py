class Test:
    def __init__(self):
        self.name = "ABC"  # public variable 
        self._marks = 23  # protected varibale
        self.__rno = 1   # private variable 


obj = Test()
print(obj.name)
print(obj._marks)

