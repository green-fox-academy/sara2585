class Currency:
    def __init__(self, code, bank, value):
        pass

class USADollar(Currency):
    def __init__(self, value, code = "USD", bank = "Federal Reserve System"):
        self.code = code
        self.bank = bank
        self.value = value

class HungarianForint(Currency):
    def __init__(self, value, code = "HUF", bank = "Hungarian National Bank"):
        self.code = code
        self.bank = bank
        self.value = value

class BankAccount:
    def __init__(self, name, pin, currency ):
        self.name = name
        self.pin = pin
        self.currency = currency
    def deposit(self, value):
        if value > 0:
            self.currency.value += value
    def withdraw(self, pin, amount):
        if pin == self.pin and amount <= self.currency.value:
            self.cCurrency.value -= amount
            return amount
        else:
            return 0

class Bank:
    def __init__(self, bankaccountlist=[]):
        self.bankaccountlist = bankaccountlist

    def createAccount(self, bankaccount):
        self.bankaccountlist.append(bankaccount)

    def getAllMoney(self):
        sum = 0
        for i in self.bankaccountlist:
            sum += i.currency.value
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


        
