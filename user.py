from bankaccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.04, 5000)
        

    def deposit(self, amount):
        self.account.deposit(amount)

        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}\nBalance: ${self.account.balance}")


new_user = User("Max", "max@max.com")
new_user.deposit(.50).display_user_balance()
new_user.withdraw(2).display_user_balance()


