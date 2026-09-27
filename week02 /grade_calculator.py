total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")
    
    if name == 'q':
        break
        
    score_input = float(input("Enter score: "))
    
    if score_input < 0 or score_input > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue
        
    if score_input >= 90:
        letter_grade = 'A'
    elif score_input >= 80:
        letter_grade = 'B'
    elif score_input >= 70:
        letter_grade = 'C'
    elif score_input >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    print(f"{name}: {int(score_input)} -> {letter_grade}")
    total_score += score_input
    student_count += 1

if student_count > 0:
    average_score = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average_score:.2f}")
else:
    print("No students entered.")
