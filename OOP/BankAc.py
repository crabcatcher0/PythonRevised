class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        total = self.balance + amount 

        with open("deposite.txt", "w") as file:
            file.write(f"{amount}$ is deposited. Total balance is {total}$.")
        return f"Please check the recipt."
            
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance.")
        else:
          reduced = self.balance - amount

          with open("withdraw.txt", "w") as file:
            file.write(f"{amount}$ has been withdraw. \nTotal balance is {reduced}$.")
          
        return f"Please check the recipt."
    
r = BankAccount("Ram", 200)
print(r.withdraw(50))