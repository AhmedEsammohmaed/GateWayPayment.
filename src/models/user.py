import pickle
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, bank_name: str, user_id: int, password: str, name: str, phone: int, email: str, balance: float):
        self.bank_name = bank_name
        self.user_id = user_id
        self._password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.balance = balance

    def check_password(self, password: str) -> bool:
        return self._password == password

    def add_balance(self, amount: float):
        self.balance += amount

    def deduct_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    @abstractmethod
    def get_payment_method(self) -> str:
        pass

    def __str__(self):
        return f"{self.name} ({self.bank_name}) - Balance: ${self.balance:.2f}"
