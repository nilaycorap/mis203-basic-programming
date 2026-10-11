import matplotlib.pyplot as plt
import random

# Smart Expense Tracker
# A simple Python project

expenses = {
    "Food": 150,
    "Transport": 50,
    "Coffee": 80,
    "Shopping": 200,
    "Other": 70
}

print("SMART EXPENSE TRACKER")
print("---------------------")

# Display all expenses
for category, amount in expenses.items():
    print(f"{category}: {amount} TL")

# Calculate total expenses
total = sum(expenses.values())

print("---------------------")
print(f"Total expenses: {total} TL")

# Find the highest expense
highest = max(expenses, key=expenses.get)

print(f"Highest expense: {highest}")
print(f"Amount: {expenses[highest]} TL")

# Create random colors for the chart
colors = [
    (random.random(), random.random(), random.random())
    for _ in expenses
]

# Create a pie chart
plt.figure(figsize=(8, 6))

plt.pie(
    expenses.values(),
    labels=expenses.keys(),
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("My Daily Expenses")
plt.show()
