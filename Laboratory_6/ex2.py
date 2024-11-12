# Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self.balance -= amount

if __name__ == '__main__':
    savings_account = SavingsAccount(1, 1000)
    savings_account.deposit(100)
    print("Savings account balance:", savings_account.get_balance())
    print("Savings account interest:", savings_account.calculate_interest())
    print()

    checking_account = CheckingAccount(2, 1000)
    checking_account.deposit(100)
    print("Checking account balance:", checking_account.get_balance())
    checking_account.withdraw(200)
    print("Checking account balance:", checking_account.get_balance())