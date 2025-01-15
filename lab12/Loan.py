from Balance import Balance

class Loan:
    def __init__(self, loan_ammount: float, interest_rate: float, months: int):
        self.loan_ammount = loan_ammount
        self.interest_rate = interest_rate
        self.months = months
        self.total_ammount = loan_ammount * (1 + interest_rate / 100) 
        self.balance = Balance(self.total_ammount)

    def calculatePayment(self):
        return self.total_ammount / self.months
    
    def pay(self, value):
        return self.balance.change(-value)
    
    def isPaidOff(self):
        return self.balance.get() == 0
