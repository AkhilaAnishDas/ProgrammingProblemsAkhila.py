class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Balance:", self.balance)


# Example
acc = BankAccount("Akhila", 500)
acc.deposit(200)
acc.withdraw(100)
acc.check_balance()
