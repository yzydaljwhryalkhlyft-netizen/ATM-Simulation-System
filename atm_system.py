import time
import os

# File to store balance data on your phone storage
DATA_FILE = "atm_data.txt"

def load_balance():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return float(file.read().strip())
    return 1000.0  # Default initial balance

def save_balance(balance):
    with open(DATA_FILE, "w") as file:
        file.write(str(balance))

def main_atm():
    balance = load_balance()
    correct_pin = "1234"
    attempts = 0
    
    print("====================================")
    print("    WELCOME TO SMART ATM SYSTEM     ")
    print("        [ Mobile Optimized ]        ")
    print("====================================")
    
    while attempts < 3:
        user_pin = input("Please Enter Your 4-Digit PIN: ")
        if user_pin == correct_pin:
            print("\n✔ PIN Verified Successfully!")
            break
        else:
            attempts += 1
            print(f"❌ Incorrect PIN. Attempts remaining: {3 - attempts}\n")
            
    if attempts == 3:
        print("❗ Account Locked. Please contact support.")
        return

    while True:
        print("\n----- SELECT TRANSACTION -----")
        print("1. 💵 Check Balance")
        print("2. 💰 Deposit Money")
        print("3. 💸 Withdraw Money")
        print("4. ❌ Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(f"\n💵 Current Balance: ${balance:.2f}")
            
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    save_balance(balance)
                    print(f"✔ Successfully deposited ${amount:.2f}")
                    print(f"💵 New Balance: ${balance:.2f}")
                else:
                    print("❗ Amount must be greater than zero.")
            except ValueError:
                print("❗ Invalid input. Enter a valid number.")
                
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > balance:
                    print("❗ Insufficient funds!")
                elif amount <= 0:
                    print("❗ Amount must be greater than zero.")
                else:
                    balance -= amount
                    save_balance(balance)
                    print("\n🔄 Processing withdrawal...")
                    time.sleep(1)
                    print("✔ Withdrawal Successful!")
                    print(f"💵 Remaining Balance: ${balance:.2f}")
            except ValueError:
                print("❗ Invalid input. Enter a valid number.")
                
        elif choice == "4":
            print("\nThank you for using our ATM services. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main_atm()
    
