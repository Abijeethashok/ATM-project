class atm:
    def __init__ (self,initialcash,accountno):
        self.initialcash = initialcash
        self.accountno = accountno

    def checkbalance(self):
        print(self.initialcash)
    
    def cashdiposit(self,money):
        self.initialcash = self.initialcash + money

    def cashwithdraw(self,withdraw):
        self.initialcash = self.initialcash - withdraw

atm1 = atm(5000,1234567890)

atm1.cashdiposit(1000)

atm1.checkbalance()

atm1.cashwithdraw(500)

atm1.checkbalance()

