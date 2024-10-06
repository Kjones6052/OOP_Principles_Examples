class BankAccount:
    def __init__(self, account_holder, initial_balance):
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

    def withdraw(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest {interest} add to the balance.")

    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded")
        else:
            super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, transaction_fee):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.get_balance():
            self.set_balance(self.get_balance() - total_amount)
            print(f"Withdrawn: {amount}, Transaction fee: {self.transaction_fee}")
        else:
            print("Insufficient balance for withdrawal and transaction fee.")

savings = SavingsAccount("Alice", 1500, 0.05)
checking = CheckingAccount("Bob", 2000, 20)

savings.add_interest()
savings.withdraw(200)
print(f"Savings Account Balance: {savings.get_balance()}")

checking.deposit(500)
checking.withdraw(300)
print(f"Checking Account Balance: {checking.get_balance}")

savings.set_account_holder("Alice Smith")
checking.set_account_holder("Bob Johnson")