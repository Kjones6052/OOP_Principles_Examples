class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__balance = initial_balance
        self.account_holder = account_holder

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_account_holder(self):
        return self.account_holder
    
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

account = BankAccount("Alex", 1000)
print(f"Account Holder: {account.get_account_holder()}")
print(f"Initial Balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
print(f"Updated Balance: {account.get_balance()}")

account.set_account_holder("Charlie")
print(f"New Account Holder: {account.get_account_holder()}")