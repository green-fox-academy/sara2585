class Currency:
    def __init__(self, code, bank, value):
        self.code = code
        self.bank = bank
        self.value = value

class USADollar(Currency):
    def __init__(self, value, code = "USD", bank = "Federal Reserve System"):
        Currency.__init__(self, code, bank, value)


class HungarianForint(Currency):
    def __init__(self, value, code = "HUF", bank = "Hungarian National Bank"):
        Currency.__init__(self, code, bank, value)
        

class BankAccount:
    def __init__(self, name, pin, Currency ):
        self.name = name
        self.pin = pin
        self.Currency = Currency
    def deposit(self, value):
        if value > 0:
            self.Currency.value += value
    def withdraw(self, pin, amount):
        if pin == self.pin and amount <= self.Currency.value:
            self.Currency.value -= amount
            return amount
        else:
            return 0

class Bank:
    def __init__(self, bankaccountlist=[]):
        self.bankaccountlist = bankaccountlist

    def createAccount(self, BankAccount):
        self.bankaccountlist.append(BankAccount)

    def getAllMoney(self):
        sum = 0
        for i in self.bankaccountlist:
            sum += i.Currency.value
        return f"The sum of all account money is: {sum}"
    

    

USD = USADollar(500)
bankaccount1 = BankAccount("Sara", "010", USD)
bankaccount1.deposit(100)
# print(bankaccount1.Currency.value)

# print(bankaccount1.withdraw("010", 800))

bankaccount2 = BankAccount("Daisy", "020", HungarianForint(1000))
bankaccount2.deposit(500)

bank = Bank()
bank.createAccount(bankaccount1)
bank.createAccount(bankaccount2)

print(bank.getAllMoney())


        
