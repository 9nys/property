class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Invalid balance! Balance cannot be negative.")


my_account = Account(1000)

print("Current balance:", my_account.balance)

my_account.balance = 1500
print("Updated balance:", my_account.balance)


my_account.balance = -500
