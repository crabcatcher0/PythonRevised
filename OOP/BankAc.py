class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        total = amount + self.balance
        return f"Balance Added. Current balance is {total}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance.")
        reduced = amount - self.balance
        return reduced
    
r = BankAccount("Ram", 200)
print(r.withdraw(400))