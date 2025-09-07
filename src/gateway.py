from typing import Dict
from src.models.user import User
from src.services import storage

class PaymentGateway:
    def __init__(self):
        self.users: Dict[int, User] = storage.load_users()
        if not self.users:  # Seed users if file is empty
            from src.models.visa import Visa
            from src.models.wallet import Wallet

            self.users[1] = Visa("NBE", 1, "ahmed", "Ahmed", 1000, "ahmed@gmail.com", 500.0)
            self.users[2] = Wallet("NBE", 2, "esam", "Esam", 1001, "esam@gmail.com", 300.0, wallet_id=2001)
            self.users[3] = Visa("NBE", 3, "mohamed", "Mohamed", 1002, "mohamed@gmail.com", 700.0)
            storage.save_users(self.users)

    def authenticate(self, user_id: int, password: str) -> User | None:
        user = self.users.get(user_id)
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def save(self):
        storage.save_users(self.users)
