import unittest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_withdraw(self):
        account = BankAccount(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_insufficient_balance(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

if __name__ == '__main__':
    unittest.main()
