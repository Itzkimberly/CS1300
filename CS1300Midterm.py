# Problem 1: Temperature Converter
# Converts between Celsius and Fahrenheit

# Get input from user
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").strip().upper()

# Validate scale and perform conversion
if scale == "C":
    # Convert Celsius to Fahrenheit
    fahrenheit = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {fahrenheit:.1f}°F")
elif scale == "F":
    # Convert Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {celsius:.1f}°C")
else:
    # Invalid scale entered
    print("Invalid scale.")
    
    # Problem 2: String Analyzer
# Analyzes character composition of a sentence

sentence = input("Enter a sentence: ")

# Initialize counters
total_chars = len(sentence)
uppercase = 0
lowercase = 0
digits = 0
spaces = 0

# Iterate through each character to count types
for char in sentence:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

# Print analysis results
print(f"Total characters: {total_chars}")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Reversed: {sentence[::-1]}")

# Problem 3: List Operations Toolkit
# Demonstrates various list operations

numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

# 1. Print original list
print(f"Original: {numbers}")

# 2. Print first and last elements
print(f"First: {numbers[0]}, Last: {numbers[-1]}")

# 3. Print middle 4 elements (indices 3-6)
print(f"Middle 4: {numbers[3:7]}")

# 4. Append 99 to the end
numbers.append(99)
print(f"After append 99: {numbers}")

# 5. Insert 0 at the beginning
numbers.insert(0, 0)
print(f"After insert 0 at start: {numbers}")

# 6. Remove value 42
numbers.remove(42)
print(f"After remove 42: {numbers}")

# 7. Pop last element and print what was removed
popped = numbers.pop()
print(f"Popped: {popped}")
print(f"After pop: {numbers}")

# 8. Check if 23 is in list
print(f"Is 23 in list? {23 in numbers}")

# 9. Print index of value 16
print(f"Index of 16: {numbers.index(16)}")

# 10. Print final list and length
print(f"Final list: {numbers}")
print(f"Length: {len(numbers)}")

# Problem 4: Course Eligibility Checker
print("\n--- Problem 4: Course Eligibility ---")
gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq = input("Prerequisite completed? (yes/no): ").strip().lower() == "yes"

if gpa >= 3.5 and credits >= 60 and prereq:
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60:
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

print(status)
print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {'Yes' if prereq else 'No'}")
print(f"Status: {status}")
print("-" * 28)

# Problem 5: Student Roster Manager
# Manages class roster with parallel lists

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1: Print formatted roster
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    # Format with number, left-aligned name (10 chars), and score
    print(f"{i+1}. {names[i]:<10} - {scores[i]}")
print("=" * 20)

# Task 2: Find highest and lowest scores without max()/min()
highest_idx = 0
lowest_idx = 0

for i in range(1, len(scores)):
    if scores[i] > scores[highest_idx]:
        highest_idx = i
    if scores[i] < scores[lowest_idx]:
        lowest_idx = i

print(f"Highest: {names[highest_idx]} - {scores[highest_idx]}")
print(f"Lowest: {names[lowest_idx]} - {scores[lowest_idx]}")

# Task 3: Calculate class average
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Class Average: {average:.2f}")

# Task 4: Determine letter grades
print("--- Grade Report ---")
for i in range(len(names)):
    score = scores[i]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{names[i]}: {score} -> {grade}")

# Task 5: Add Frank and remove Diana
names.append("Frank")
scores.append(77)

# Find and remove Diana
diana_idx = names.index("Diana")
names.pop(diana_idx)
scores.pop(diana_idx)

print(f"Updated roster length: {len(names)}")