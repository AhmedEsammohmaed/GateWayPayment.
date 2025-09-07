from src.models.user import User

class TransactionService:
    @staticmethod
    def transfer(sender: User, receiver: User, amount: float) -> bool:
        if sender.deduct_balance(amount):
            receiver.add_balance(amount)
            return True
        return False
