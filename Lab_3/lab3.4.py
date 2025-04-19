class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self._balance += amount
        self._transactions.append(f"+{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте.")
        self._balance -= amount
        self._transactions.append(f"-{amount}")

    @property
    def balance(self):
        return self._balance

    def log_transactions(self):
        print("\nИстория транзакций:")
        for t in self._transactions:
            print(t)