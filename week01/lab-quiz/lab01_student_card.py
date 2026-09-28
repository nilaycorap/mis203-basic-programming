# lab01_student_card.py

print("--- Student Introduction Card Generator ---")

# Collect 5 pieces of information from the user
name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
github_username = input("Enter your GitHub username: ")
programming_goal = input("Enter one programming goal: ")

# Display the clear, formatted student card using f-strings
print("\n" + "=" * 45)
print("             STUDENT INTRODUCTION CARD             ")
print("=" * 45)
print(f"Name:       {name}")
print(f"Student ID: {student_id}")
print(f"Department: {department}")
print(f"GitHub:     @{github_username}")
print(f"Goal:       {programming_goal}")
print("=" * 45)
