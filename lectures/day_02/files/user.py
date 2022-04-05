class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self


    def display_balance(self):
        pass
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)



armen = User('Armen', 'adog@aol.com')
noah = User("Noah", "noah@emial.com")

armen.make_withdrawal(500)
print(armen.account_balance)
armen.transfer_money(noah, 325)
print(armen.account_balance)
print(noah.account_balance)

print(armen.make_deposit(500))
armen.make_deposit(1000).make_withdrawal(1000)
