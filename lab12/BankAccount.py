from Balance import Balance
from Loan import Loan

# TODO

class BankAccount:
    def __init__(self, first_name, last_name, pesel, account_number, initialBalance):
        self._first_name = first_name
        self._last_name = last_name
        self._pesel = pesel
        self._account_number = account_number
        self._balance = Balance(initialBalance)
        self.loans = []

    def deposit(self, value):
        self._balance.change(value)

    def withdraw(self, value):
        self._balance.change(-value)

    def createLoan(self, ammount, months, interestRate):
        loan = Loan(self, ammount, months, interestRate)
        self.loans.append(loan)
        return loan
    
    def getLoans(self):
        return self.loans
    
    def payLoan(self, loan_index):
        if 0 <= loan_index < len(self.loans):
            loan = self.loans[loan_index]
            payment = self.calculatePayment()
            if self._balance.get() >= payment:
                if loan.pay(payment):
                    return True
        return False