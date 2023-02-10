class bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"{self.owner} have: {self.balance}"
    def deposit(self, deposit):
        b = int(self.balance)
        d = int(deposit)
        b = int(b + d)
        print("Your current balance is ")
        print(b)


bn = bank("Ilyas")
print(bn)
print("input moneys")
s = input()
bn.deposit(s)
