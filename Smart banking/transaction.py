# transaction.py

from datetime import datetime

class Transaction:
    def __init__(self, acc_no, t_type, amount):
        self.acc_no = acc_no
        self.t_type = t_type
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"{self.date} | {self.t_type} | {self.amount}"