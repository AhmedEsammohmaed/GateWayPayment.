import pickle
from typing import Dict
from src.models.user import User

DATA_FILE = "user_balances.pkl"

def save_users(users: Dict[int, User]):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(users, f)

def load_users() -> Dict[int, User]:
    try:
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return {}

