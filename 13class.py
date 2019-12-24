class Account:
    interest = 0.02 # interest is a class attribute, share with all instances though the value may change
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder # balance, holder are object attributes
    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient fund'
        self.balance = self.balance - amount
        return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
jc = Account('John')
balance = getattr(jc, 'balance')
balance = Account.deposit(jc, 10) # deposit function has two parameter
balance = jc.deposit(10) # deposit method, automaticlly bind jc to self. method invoked on object jc
jm = Account('Jim')
#>>> jm.interest
#0.02
#>>> Account.interest
#0.02       # instance attribute
#>>> jc.interest = 0.04
#>>> Account.interest
#0.02    # class attribute wou't change by instance attribute
#>>> Account.interest = 0.01
#>>> jm.interest
#0.01    # class attribute share by all instance
#>>> jc.interest
#0.04     # first match the name to instance attribute, if can't find, find among the class attributes

class Checking_account(Account):      # override interest, withdraw attributes, inherite other behaviour
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
jkc = Checking_account('Jim')   # try to find name in instance-- in current class-- in base class
jkc.deposit(10) # self bound to Checking_account class
class Saving_account(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
def deposit_all(winners, amount = 5):
    for account in winners:
        account.deposit(5)
class AsSeenOnTV_account(Checking_account, Saving_account):
    def __init__(self,account_holder):
        self.balance = 1
        aelf.holder = account_holder
"""
class bank:
    def __init__(self):
        self.accounts = []
    def open(self, holder, amount, type = Account):
        account = type()
        account.deposit(amount)
        self.accounts.append(account)
        return account
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)
    def too_big_to_fail(self):
        return len(self.accounts) > 1
"""
