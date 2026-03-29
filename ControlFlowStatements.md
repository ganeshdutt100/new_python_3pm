Conditional Statements
Conditional statements help execute different blocks of code based on
conditions.

1. if Statement

   # Executes a block of code if the condition is True.

   age = 18
   if age >= 18:
   print("You are eligible to vote!")
   Output:
   You are eligible to vote!

2. if-else Statement

   # Executes one block if the condition is True, otherwise executes another block.

   num = int(input("Enter a number: "))
   if num % 2 == 0:
   print("Even number")
   else:
   print("Odd number")

   Input: 7
   Output:
   Odd number

3. elif Statement (Multiple Conditions)

# Executes multiple conditions in sequence.

marks = int(input("Enter your marks: "))
if marks >= 90:
print("Grade: A")
elif marks >= 75:
print("Grade: B")
elif marks >= 60:
print("Grade: C")
else:
print("Grade: F")

Input: 85
Output:
Grade: B

4. Nested if Statement
   # An if statement inside another if statement.
   num = int(input("Enter a number: "))
   if num >= 0:
   if num == 0:
   print("The number is zero")
   else:
   print("The number is positive")
   else:
   print("The number is negative")
   Input: -5
   Output:
   The number is negative
