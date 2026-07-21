def show_balance():
    print(f"Your current balance is: ${balance:.2f}")
def deposit():
    amount = float(input("Enter the amount to deposit: $  "))

    if amount < 0:
        print("Deposit amount must be a positive number. Please try again.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw: $  "))

    if amount < 0:
        print("Withdrawal amount must be a positive number. Please try again.")
        return 0
    elif amount > balance:
        print("Insufficient funds. Please try again.")
        return 0
    else:
        return amount

def transfer():
    amount = float(input("Enter the amount to transfer: $  "))

    if amount < 0:
        print("Transfer amount must be a positive number. Please try again.")
        return 0
    elif amount > balance:
        print("Insufficient funds. Please try again.")
        return 0
    else:
        recipient_account = input("Enter the recipient's account number: ")
        # Return both amount and recipient so the caller can update balance
        return amount, recipient_account

balance = 0
is_running = True

while is_running:
    print("Welcome to the Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        result = transfer()
        if result:
            amount, recipient = result
            balance -= amount
            print(f"Successfully transferred ${amount:.2f} to account {recipient}.")
    elif choice == '5':
        print("Thank you for using the Banking Program. Have a great day!")
        break
    else:
        print("Invalid option. Please try again.")
