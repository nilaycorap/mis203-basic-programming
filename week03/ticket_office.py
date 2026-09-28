# Initialize summary tracking variables
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    # 1. Ask for customer name or quit signal
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == 'q':
        break

    # 2. Ask for age and validate boundaries (0 to 120)
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    # 3. Ask for day type and validate input
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    # 4. Ask for student status and validate input
    student = input("Student (yes/no): ").strip().lower()
    if student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    # 5. Determine base price according to day type
    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    # 6. Apply discount rules in order of priority
    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    # 7. Calculate final price and display result
    final_price = base_price * (1 - discount)
    print(f"{name}: {final_price:.2f} TRY ({category})")

    # 8. Update summary statistics
    tickets_sold += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

# Display summary after exiting loop
if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
