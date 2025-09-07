from src.models.user import User

class Visa(User):
    def __init__(self, bank_name, user_id, password, name, phone, email, balance):
        super().__init__(bank_name, user_id, password, name, phone, email, balance)

    def add_balance(self, amount: float):
        print("💳 Visa payment processing...")
        super().add_balance(amount)
        print("✅ Visa payment successful.")

    def get_payment_method(self) -> str:
        return "Visa"
