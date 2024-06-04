import time
from datetime import datetime

print("Please insert Your CARD")

# for card processing
time.sleep(5)

password = 1234

# taking atm pin from user
pin = int(input("Enter your ATM PIN: "))

# user account balance
balance = 5000

# transaction history
transaction_history = []

# checking pin is valid or not
if pin == password:
    # loop will run until user exits
    while True:
        # showing info to user
        print(""" 
            1 == Check Balance
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == Transfer Balance
            5 == Transaction History
            6 == Exit
            """
              )

        try:
            # taking an option from user
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue
        
        if option == 1:
            # Check Balance
            print(f"Your current balance is {balance}")
        
        elif option == 2:
            # Withdraw Balance
            try:
                withdraw_amount = int(input("Please enter withdraw amount: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    transaction = f"{datetime.now()} - Withdrawn: {withdraw_amount}"
                    transaction_history.append(transaction)
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your updated balance is {balance}")
                else:
                    print("Insufficient balance")
            except ValueError:
                print("Please enter a valid amount")
        
        elif option == 3:
            # Deposit Balance
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                transaction = f"{datetime.now()} - Deposited: {deposit_amount}"
                transaction_history.append(transaction)
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")
            except ValueError:
                print("Please enter a valid amount")
        
        elif option == 4:
            # Transfer Balance
            try:
                transfer_amount = int(input("Please enter transfer amount: "))
                target_account = input("Please enter target account number: ")
                if transfer_amount <= balance:
                    balance -= transfer_amount
                    transaction = f"{datetime.now()} - Transferred: {transfer_amount} to {target_account}"
                    transaction_history.append(transaction)
                    print(f"{transfer_amount} is transferred to account {target_account}")
                    print(f"Your updated balance is {balance}")
                else:
                    print("Insufficient balance")
            except ValueError:
                print("Please enter a valid amount")
        
        elif option == 5:
            # Transaction History
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions found.")
        
        elif option == 6:
            # Exit
            print("Thank you for using our ATM. Have a nice day!")
            break
        
        else:
            print("Invalid option, please try again")
else:
    print("Wrong PIN. Please try again.")
123