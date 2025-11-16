class BankAccount:
    def __init__(self, place_holder):
        self.place_holder = place_holder
        self.balance = 0
        self.transaction = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f'Deposited {amount}')
            print(f"{amount} deposited, new balance {self.balance}")
        else:
            print("Amount must be positve number")
       
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction.append(f"Withdrawned {amount}")
                print(f"{amount} has been withdrawned, balance {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Amount must be positive")
    def show_balance(self):
        print(f"Balance: {self.balance}")
    def show_transaction(self):
        if not self.transaction:
            print("No transaction yet")
        else:
            print("Transaction history: ")
            for t in self.transaction:
                print(f"-- {t}")

account = BankAccount("Galastoh")
account.deposit(4000)
account.withdraw(200)
account.show_balance()
account.show_transaction()


    