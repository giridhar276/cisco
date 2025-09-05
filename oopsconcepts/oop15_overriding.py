
class BankAccount:
    def interest(self):
        print("Generic bank interest 3%")

class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings Account interest 4%")

class FixedDeposit(BankAccount):
    def interest(self):
        print("Fixed Deposit interest 6%")

s = SavingsAccount()
f = FixedDeposit()
s.interest()   # 4%
f.interest()   # 6%
