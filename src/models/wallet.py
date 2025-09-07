from src.models.user import User

class Wallet(User):
    def __init__(self, bank_name, user_id, password, name, phone, email, balance, wallet_id):
        super().__init__(bank_name, user_id, password, name, phone, email, balance)
        self.wallet_id = wallet_id

    def add_balance(self, amount: float):
        print("📱 Wallet payment processing...")
        super().add_balance(amount)
        print("✅ Wallet payment successful.")

    def get_payment_method(self) -> str:
        return "Wallet"
