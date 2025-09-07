import argparse
from src.gateway import PaymentGateway
from src.services.transaction import TransactionService

def main():
    parser = argparse.ArgumentParser(description="Quantum Payment Gateway CLI")
    parser.add_argument("--sender", type=int, help="Sender user ID")
    parser.add_argument("--password", type=str, help="Sender password")
    parser.add_argument("--receiver", type=int, help="Receiver user ID")
    parser.add_argument("--amount", type=float, help="Amount to transfer")
    args = parser.parse_args()

    gateway = PaymentGateway()
    sender = gateway.authenticate(args.sender, args.password)

    if not sender:
        print("❌ Invalid user ID or password.")
        return

    receiver = gateway.get_user(args.receiver)
    if not receiver:
        print("❌ Receiver not found.")
        return

    print(f"👤 Welcome {sender.name}. Your balance: ${sender.balance:.2f}")

    if TransactionService.transfer(sender, receiver, args.amount):
        print("✅ Transaction successful!")
        print(f"💰 Sender new balance: ${sender.balance:.2f}")
        print(f"💰 Receiver new balance: ${receiver.balance:.2f}")
        gateway.save()
    else:
        print("❌ Insufficient balance.")

if __name__ == "__main__":
    main()
