class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def show_account(self):
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


# Child Class 1
class SavingAccount(Account):
    def __init__(self, acc_no, name, balance, interest):
        super().__init__(acc_no, name, balance)
        self.interest = interest

    def show_saving(self):
        self.show_account()
        print("Interest Rate:", self.interest, "%")


# Child Class 2
class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance, interest):
        super().__init__(acc_no, name, balance)
        self.interest = interest

    def show_current(self):
        self.show_account()
        print("Interest Rate:", self.interest)


# Object Creation
s = SavingAccount(101, "Amit", 50000, 3)
c = CurrentAccount(102, "Ravi", 30000, 4)

print("Saving Account Details:")
s.show_saving()

print("\nCurrent Account Details:")
c.show_current()

    