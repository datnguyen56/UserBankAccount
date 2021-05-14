class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.account.acc_balance}")
        return self

class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = 0
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        self.balance = self.balance * 0.01
        return self

account1 = BankAccount(0, 0)
account2 = BankAccount(0, 0)

account1.deposit(300).deposit(500).deposit(900).withdraw(400).display_account_info().yield_interest()

account2.deposit(1100).deposit(500).withdraw(300).withdraw(150).withdraw(200).withdraw(400).display_account_info().yield_interest()
