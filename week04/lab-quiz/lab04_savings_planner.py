starting_balance = float(input("Enter starting balance: "))

while starting_balance < 0:
    print("Starting balance cannot be negative.")
    starting_balance = float(input("Enter starting balance: "))

deposit = float(input("Enter monthly deposit: "))

while deposit <= 0:
    print("Deposit must be positive.")
    deposit = float(input("Enter monthly deposit: "))

rate = float(input("Enter monthly interest rate (%): "))

while rate < 0:
    print("Interest rate cannot be negative.")
    rate = float(input("Enter monthly interest rate (%): "))

goal = float(input("Enter savings goal: "))

while goal <= 0:
    print("Goal must be positive.")
    goal = float(input("Enter savings goal: "))

balance = starting_balance
total_interest = 0
month = 0

print()
print("Month   Interest   Balance")

if balance >= goal:
    print("Your goal is already reached!")
else:
    while month < 60:
        month = month + 1

        interest = balance * rate / 100
        balance = balance + interest
        total_interest = total_interest + interest

        balance = balance + deposit

        print(f"{month:<8}{interest:<11.2f}{balance:.2f}")

        if balance >= goal:
            break

if balance >= goal:
    print()
    print(f"Goal reached in {month} months.")
else:
    print()
    print("Goal not reached in 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")
