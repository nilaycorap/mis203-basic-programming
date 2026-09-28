# Student Information
* **Name:** Nilay Çorap
* **Student Number:** 2404109002
* **Department:** Management Information Systems
* **Course Name:** MIS203 Basic Programming

 AI Tool Usage
* *AI Tool Used:* ChatGPT 
* *Prompt Used:* "Write a Python script that asks the user for their name, department, age, and career goal, then prints them in a single formatted line."
* *What did you change?:* I adjusted the input prompt messages to make them clearer and added comments to explain each step of the code.
## Week 02

* **AI Tool Used:** Gemini
* **Prompt Used:** "Bu ödevi nasıl yapacağım adım adım anlatır mısın"
* **What did you change?** I carefully reviewed the generated logic to ensure all conditions, input validations, grade boundaries, and output formats fully matched the assignment instructions.
* **What does break do in your program?** The `break` statement immediately stops and exits the infinite `while True` loop as soon as the user enters 'q' for the student name.
* 
## Week 03

AI Tool Used: ChatGPT
Prompt Used: Write a Python program named ticket_office.py that sells cinema tickets in a loop, handles boundary validation (age 0-120, day type, student status), applies a single discount in priority order, and calculates summary statistics upon quitting.
What did you change? I formatted the output strings to match the exact spacing and capitalization required by the assignment, and added input validation with continue statements.

Tests:
1. Boundary Test (Age = 5): Name: "Can", Age: 5, Day: "weekend", Student: "no" -> Result: "Can: 0.00 TRY (Free)" (Free discount applies for age under 6).
2. Boundary Test (Age = 12): Name: "Deniz", Age: 12, Day: "weekday", Student: "no" -> Result: "Deniz: 120.00 TRY (Child)" (Child discount applies up to age 12).
3. Boundary Test (Age = 26): Name: "Mert", Age: 26, Day: "weekday", Student: "yes" -> Result: "Mert: 200.00 TRY (Standard)" (Exceeds student age limit of 25).

Why does the order of the rules matter?
The order matters because Python evaluates if/elif conditions sequentially and stops at the first true condition. If the Student rule came before the Child rule, a 10-year-old student would receive the 30% Student discount instead of the more favorable 40% Child discount.
