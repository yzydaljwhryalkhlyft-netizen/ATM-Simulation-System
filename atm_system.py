import time

def main_atm():
    # --------------------------------------------------
    # Period 3: Smart ATM System Implementation
    # --------------------------------------------------
    
    balance = 1000.0  # Initial default balance
    correct_pin = "1234"  # Default 4-digit PIN
    attempts = 0
    
    print("====================================")
    print("    WELCOME TO SMART ATM SYSTEM     ")
    print("              PERIOD 3              ")
    print("====================================")
    
    # Security PIN Verification
    while attempts < 3:
        user_pin = input("Please Enter Your 4-Digit PIN: ")
        if user_pin == correct_pin:
            print("\n✔ PIN Verified Successfully!")
            break
        else:
            attempts += 1
            print(f"❌ Incorrect PIN. Attempts remaining: {3 - attempts}\n")
            
    if attempts == 3:
        print("❗ Account Locked due to multiple incorrect attempts. Please contact support.")
        return

    # Main Interactive Menu
    while True:
        print("\n----- SELECT TRANSACTION -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(f"\n💵 Current Balance: ${balance:.2f}")
            
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    print(f"✔ Successfully deposited ${amount:.2f}")
                    print(f"💵 New Balance: ${balance:.2f}")
                else:
                    print("❗ Amount must be greater than zero.")
            except ValueError:
                print("❗ Invalid input. Please enter a valid number.")
                
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > balance:
                    print("❗ Insufficient funds! Transaction declined.")
                elif amount <= 0:
                    print("❗ Amount must be greater than zero.")
                else:
                    balance -= amount
                    print("\n🔄 Processing withdrawal...")
                    time.sleep(1)  # Simulated processing delay
                    print("✔ Withdrawal Successful! Please take your cash.")
                    print(f"💵 Remaining Balance: ${balance:.2f}")
            except ValueError:
                print("❗ Invalid input. Please enter a valid number.")
                
        elif choice == "4":
            print("\nThank you for using our ATM services. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main_atm()
                  
