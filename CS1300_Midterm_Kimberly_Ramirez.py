# CS1300_Midterm_Kimberly_Ramirez.py
# Problem 1: Distance Converter

# Get input from user
distance = float(input("Enter distance: "))
unit = input("Enter unit (km/mi): ").lower()  # Convert to lowercase for case-insensitive comparison

# Check if unit is valid and perform conversion
if unit == "km":
    # Convert kilometers to miles
    miles = distance * 0.621371
    print(f"{distance:.2f} km = {miles:.2f} mi")
elif unit == "mi":
    # Convert miles to kilometers
    km = distance * 1.60934
    print(f"{distance:.2f} mi = {km:.2f} km")
else:
    # Invalid unit entered
    print("Invalid unit.")

# CS1300_Midterm_Kimberly_Ramirez.py  
# Problem 2: Text Statistics Tool

# Get sentence from user
sentence = input("Enter a sentence: ")

# 1. Total characters (including spaces)
total_chars = len(sentence)

# 2. Total words (split by spaces)
words = sentence.split()
total_words = len(words)

# 3. Count vowels (both upper and lowercase)
# 4. Count consonants (letters that are not vowels)
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():  # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# 5. Average word length (total non-space characters / number of words)
# Calculate non-space characters
non_space_chars = 0
for char in sentence:
    if char != " ":
        non_space_chars += 1

if total_words > 0:
    avg_word_length = non_space_chars / total_words
else:
    avg_word_length = 0

# 6. Longest word in the sentence
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Print results
print(f"Total characters: {total_chars}")
print(f"Total words: {total_words}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Average word length: {avg_word_length:.2f}")
print(f"Longest word: {longest_word}")

# CS1300_Midterm_Kimberly_Ramirez.py
# Problem 3: Grade Book Manager

# Initial data
assignments = ["Quiz 1", "Homework 1", "Lab 1", "Quiz 2", "Homework 2"]
scores = [85, 92, 78, 88, 95]

# 1. Print the original grade book as a formatted table
print("=== GRADE BOOK ===")
for i in range(len(assignments)):
    print(f"{i + 1}. {assignments[i]} - {scores[i]}")
print("==================")

# 2. Print the highest-scoring and lowest-scoring assignments (without max() or min())
# Find highest score and its assignment
highest_score = scores[0]
highest_assignment = assignments[0]
for i in range(1, len(scores)):
    if scores[i] > highest_score:
        highest_score = scores[i]
        highest_assignment = assignments[i]

# Find lowest score and its assignment
lowest_score = scores[0]
lowest_assignment = assignments[0]
for i in range(1, len(scores)):
    if scores[i] < lowest_score:
        lowest_score = scores[i]
        lowest_assignment = assignments[i]

print(f"Highest: {highest_assignment} ({highest_score})")
print(f"Lowest: {lowest_assignment} ({lowest_score})")

# 3. Calculate and print the overall average to 2 decimal places
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Average: {average:.2f}")

# 4. Determine a letter grade for each assignment and print
print("\nLetter Grades:")
for i in range(len(assignments)):
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
    print(f"{assignments[i]}: {grade}")

# 5. Append a new assignment "Lab 2" with a score of 90
assignments.append("Lab 2")
scores.append(90)

# 6. Remove "Quiz 1" from both lists
# Find the index of "Quiz 1"
index_to_remove = -1
for i in range(len(assignments)):
    if assignments[i] == "Quiz 1":
        index_to_remove = i
        break

# Remove from both lists if found
if index_to_remove != -1:
    assignments.pop(index_to_remove)
    scores.pop(index_to_remove)

# 7. Pop the last assignment and print what was removed
removed_assignment = assignments.pop()
removed_score = scores.pop()
print(f"\nRemoved: {removed_assignment} ({removed_score})")

# 8. Print the final grade book and its length
print("\n=== FINAL GRADE BOOK ===")
for i in range(len(assignments)):
    print(f"{i + 1}. {assignments[i]} - {scores[i]}")
print(f"Length: {len(assignments)}")

# CS1300_Midterm_Kimberly_Ramirez.py
# Problem 4: Shipping Cost Calculator

# Get input from user
weight = float(input("Enter package weight (lbs): "))
destination = input("Enter destination (domestic/international): ").lower()
premium = input("Premium member? (yes/no): ").lower()

# Calculate base shipping cost based on destination and weight
cost = 0
valid_destination = True

if destination == "domestic":
    if weight <= 5:
        cost = 5.00
    elif weight <= 20:
        cost = 5.00 + (0.75 * (weight - 5))
    else:  # weight > 20
        cost = 16.25 + (0.50 * (weight - 20))
elif destination == "international":
    if weight <= 5:
        cost = 15.00
    elif weight <= 20:
        cost = 15.00 + (2.00 * (weight - 5))
    else:  # weight > 20
        cost = 45.00 + (1.50 * (weight - 20))
else:
    valid_destination = False
    print("Invalid destination.")

# Apply premium discount if applicable
if valid_destination:
    if premium == "yes":
        cost = cost * 0.5  # 50% discount
    
    # Print shipping label
    print("--- Shipping Label ---")
    print(f"Weight: {weight:.2f} lbs")
    # Capitalize first letter of destination for display
    if destination == "domestic":
        display_dest = "Domestic"
    else:
        display_dest = "International"
    print(f"Destination: {display_dest}")
    # Capitalize first letter of premium for display
    if premium == "yes":
        display_premium = "Yes"
    else:
        display_premium = "No"
    print(f"Premium member: {display_premium}")
    print(f"Shipping cost: ${cost:.2f}")
    print("----------------------")

# CS1300_Midterm_Kimberly_Ramirez.py  
# Problem 5: Student Attendance Tracker
 
 # Initial data
students = ["Maria", "James", "Priya", "Tom", "Lena", "Oscar"]
attended = [18, 12, 20, 15, 9, 17]
TOTAL_CLASSES = 20

# Task 1: Print a formatted attendance roster
print("=== ATTENDANCE ROSTER ===")
for i in range(len(students)):
    percentage = (attended[i] / TOTAL_CLASSES) * 100
    print(f"{i + 1}. {students[i]} - {attended[i]}/{TOTAL_CLASSES} ({percentage:.1f}%)")
print("=========================")

# Task 2: Find and print best and worst attendance (without max() or min())
# Find best attendance
best_index = 0
for i in range(1, len(attended)):
    if attended[i] > attended[best_index]:
        best_index = i

# Find worst attendance
worst_index = 0
for i in range(1, len(attended)):
    if attended[i] < attended[worst_index]:
        worst_index = i

print(f"Best attendance: {students[best_index]} ({attended[best_index]}/{TOTAL_CLASSES})")
print(f"Worst attendance: {students[worst_index]} ({attended[worst_index]}/{TOTAL_CLASSES})")

# Task 3: Calculate and print class average attendance percentage to 1 decimal place
total_attended = 0
for num in attended:
    total_attended += num
average_attendance = total_attended / len(attended)
average_percentage = (average_attendance / TOTAL_CLASSES) * 100
print(f"Class average: {average_percentage:.1f}%")

# Task 4: Determine attendance status for each student
print("\nAttendance Status:")
for i in range(len(students)):
    percentage = (attended[i] / TOTAL_CLASSES) * 100
    if percentage >= 90:
        status = "Excellent"
    elif percentage >= 75:
        status = "Good"
    elif percentage >= 60:
        status = "At Risk"
    else:
        status = "Intervention Required"
    print(f"{students[i]}: {status}")

# Task 5: Add new student "Nina" with 16 classes, remove "Lena", print updated length
students.append("Nina")
attended.append(16)

# Find and remove "Lena"
lena_index = -1
for i in range(len(students)):
    if students[i] == "Lena":
        lena_index = i
        break

if lena_index != -1:
    students.pop(lena_index)
    attended.pop(lena_index)

print(f"\nUpdated roster length: {len(students)}")