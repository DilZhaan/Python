class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Account balance: ${self.balance}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, owner, initial_balance=0):
        if account_number not in self.accounts:
            account = BankAccount(account_number, owner, initial_balance)
            self.accounts[account_number] = account
            return f"Account created for {owner} with account number {account_number}."
        else:
            return "Account number already exists."

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found."

# Example usage
bank = Bank("MyBank")

print(bank.create_account("123456", "Alice", 1000))
print(bank.create_account("789012", "Bob", 500))

alice_account = bank.get_account("123456")
print(alice_account.deposit(200))
print(alice_account.get_balance())
print(alice_account.withdraw(300))
print(alice_account.get_balance())

bob_account = bank.get_account("789012")
print(bob_account.get_balance())
print(bob_account.withdraw(600))

print(bank.get_account("999999"))  # Account not found
