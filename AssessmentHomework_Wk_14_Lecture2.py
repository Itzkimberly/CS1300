# UNIT 1 EXERCISES
# Unit 1 - Beginner Exercise
# -----------------------------------------------------------------------------
rgb_color = (255, 128, 0)

# Print each color channel
print("=== Unit 1: Beginner ===")
print(f"Red:   {rgb_color[0]}")
print(f"Green: {rgb_color[1]}")
print(f"Blue:  {rgb_color[2]}")

# Create palette list and add color
palette = []
palette.append(rgb_color)
print(f"Palette: {palette}")


# -----------------------------------------------------------------------------
# Unit 1 - Intermediate Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 1: Intermediate ===")

# Create student tuples
student1 = ("Alice", 95, 20)
student2 = ("Bob", 87, 21)
student3 = ("Charlie", 92, 19)

# Store in classroom list
classroom = [student1, student2, student3]

# Print second student's name using double subscripting
print(f"Second student's name: {classroom[1][0]}")

# Unpack first student's information
name, grade, age = classroom[0]

# Print formatted message
print(f"{name} is {age} years old with a grade of {grade}")


# -----------------------------------------------------------------------------
# Unit 1 - Advanced Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 1: Advanced ===")

# Create original student tuple
original_student = ("Alice", [85, 90, 78], "B")

# Add fourth exam score (use a copy so original stays intact)
updated_scores = original_student[1].copy()
updated_scores.append(92)

# Calculate new average
average = sum(updated_scores) / len(updated_scores)

# Determine updated final grade
if average >= 90:
    new_grade = "A"
elif average >= 80:
    new_grade = "B"
elif average >= 70:
    new_grade = "C"
elif average >= 60:
    new_grade = "D"
else:
    new_grade = "F"

# Create new tuple with updated final grade
updated_student = (original_student[0], updated_scores, new_grade)

# Print both tuples
print(f"Original: {original_student}")
print(f"Updated:  {updated_student}")


# =============================================================================
# UNIT 2 EXERCISES
# =============================================================================

# -----------------------------------------------------------------------------
# Unit 2 - Beginner Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 2: Beginner ===")

# Create a list of three homework grades
grades = [85, 90, 78]

# Create a tuple representing today's date (month, day, year)
today = (4, 19, 2026)

# Function that boosts each grade by 5 points
def boost_grades(grade_list, bonus=5):
    for i in range(len(grade_list)):
        grade_list[i] += bonus

# Call the function and print result
boost_grades(grades)
print(f"Boosted grades: {grades}")
print(f"Today's date:   {today}")

# Explanation:
# We use a LIST for grades because they change frequently (mutable).
# We use a TUPLE for the date because it is fixed and should never change (immutable).


# -----------------------------------------------------------------------------
# Unit 2 - Intermediate Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 2: Intermediate ===")

def find_range(*args):
    """Accepts any number of numeric arguments and returns (min, max)."""
    if len(args) == 0:
        return (0, 0)
    return (min(args), max(args))

# Test with 3 numbers
print(f"Range of 3 nums:  {find_range(10, 5, 25)}")

# Test with 7 numbers
print(f"Range of 7 nums:  {find_range(8, 2, 15, 9, 4, 20, 11)}")

# Unpack a list using the * operator
test_scores = [78, 92, 85, 88, 91]
print(f"Range of scores:  {find_range(*test_scores)}")


# -----------------------------------------------------------------------------
# Unit 2 - Advanced Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 2: Advanced ===")

def calculate_statistics(*args):
    """Returns a tuple of (count, sum, average)."""
    if len(args) == 0:
        return (0, 0, 0.0)
    count = len(args)
    total = sum(args)
    average = total / count
    return (count, total, average)


def update_student_records(records, bonus):
    """
    Takes a list of student tuples [(name, grade), ...] and a bonus amount.
    Returns a NEW list with updated grades (original tuples are immutable).
    """
    updated = []
    for name, grade in records:
        updated.append((name, grade + bonus))
    return updated


# Demonstrate calculate_statistics
stats = calculate_statistics(85, 90, 78, 92)
print(f"Statistics: {stats}")

# Demonstrate update_student_records
classroom = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
print(f"Original records: {classroom}")

new_classroom = update_student_records(classroom, 5)
print(f"Updated records:  {new_classroom}")
print(f"Original intact:  {classroom}")


# =============================================================================
# UNIT 3 EXERCISES
# =============================================================================

# -----------------------------------------------------------------------------
# Unit 3 - Beginner Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 3: Beginner ===")

# Create a 3x3 grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the entire grid
print(f"Grid: {grid}")

# Print just the center number using double indexing
print(f"Center number: {grid[1][1]}")

# Use nested loops to print each row on a separate line
print("Grid rows:")
for row in grid:
    for value in row:
        print(value, end=" ")
    print()


# -----------------------------------------------------------------------------
# Unit 3 - Intermediate Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 3: Intermediate ===")

scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

# List comprehension: only passing grades (60 or above)
passing_grades = [s for s in scores if s >= 60]
print(f"Passing grades: {passing_grades}")

# List comprehension: convert passing grades to letters
def to_letter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "D"

letter_grades = [to_letter(g) for g in passing_grades]
print(f"Letter grades:  {letter_grades}")


# -----------------------------------------------------------------------------
# Unit 3 - Advanced Exercise
# -----------------------------------------------------------------------------
print("\n=== Unit 3: Advanced ===")

# Create a 4x4 multiplication table using nested list comprehension
mult_table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

# Print it in a formatted way
print("4x4 Multiplication Table:")
for row in mult_table:
    for val in row:
        print(f"{val:4}", end="")
    print()


# Function to sum diagonal elements (top-left to bottom-right)
def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total


# Test with the multiplication table
print(f"Diagonal sum: {sum_diagonal(mult_table)}")

# Generator expression that yields only even numbers from the entire table
even_gen = (val for row in mult_table for val in row if val % 2 == 0)

# Print the first 5 values
print("First 5 even values from table:")
for _ in range(5):
    print(next(even_gen))