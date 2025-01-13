class Balance:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def change(self, amount):
        if amount < 0 and self._balance + amount < 0:
            return False
        self._balance += amount
        return True

    def get(self):
        return self._balance
    
