principle = 0
rate = 0
time = 0

while True:
    try:
        principle = float(input("Enter the principal amount: "))
        if principle < 0:
            print("Principal amount must be a positive number. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        rate = float(input("Enter the interest rate: "))
        if rate < 0:
            print("Interest rate must be a positive number. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        time = int(input("Enter the time: "))
        if time < 0:
            print("Time must be a positive integer. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

total_amount = principle * (1 + (rate / 100)) ** time
print(f"The total amount after {time} years is: {total_amount:.2f}")
