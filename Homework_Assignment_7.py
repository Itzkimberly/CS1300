"""
Student Grade Tracker - CS 1300 Lecture 5 Mini-Project
A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and displays
a formatted report.

Functions:
    get_student_name — Prompt for and return student name
    is_valid_score — Helper: validate a single score
    get_exam_scores — Collect n exam scores with validation
    get_validated_scores — Helper: retry loop for score entry
    calculate_average — Compute mean of a scores list
    determine_letter_grade — Map average to letter grade
    determine_standing — Map average to academic standing
    print_divider — Helper: print a decorative line
    display_report — Print the formatted grade report
    main — Orchestrate the full program
    test_grade_tracker — Run all unit tests
"""


def get_student_name():
    """
    Prompt for and return student name.

    Returns:
        str: The student's name entered by user
    """
    return input("Student name: ")


def is_valid_score(score_str):
    """
    Helper: validate a single score string.

    Args:
        score_str (str): String to validate

    Returns:
        bool: True if valid integer between 0 and 100, False otherwise
    """
    if not score_str.isdigit():
        return False
    score = int(score_str)
    return 0 <= score <= 100


def get_validated_scores(prompt, validator, error_msg):
    """
    Helper: get input with validation and retry loop.

    Args:
        prompt (str): Input prompt to display
        validator (function): Function that returns True if input is valid
        error_msg (str): Message to show on invalid input

    Returns:
        str: Validated input string
    """
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_msg)


def get_exam_scores(n):
    """
    Collect n exam scores from user with validation.

    Args:
        n (int): Number of exam scores to collect

    Returns:
        list: List of validated integer scores
    """
    scores = []
    for i in range(n):
        score_str = get_validated_scores(
            f"Exam {i + 1} score: ",
            is_valid_score,
            "Invalid! Score must be 0-100."
        )
        scores.append(int(score_str))
    return scores


def calculate_average(scores):
    """
    Compute mean of a scores list.

    Args:
        scores (list): List of numeric scores

    Returns:
        float: Average of scores, or 0 if list is empty
    """
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def determine_letter_grade(average):
    """
    Map average to letter grade.

    Args:
        average (float): Numeric average score

    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def determine_standing(average):
    """
    Map average to academic standing.

    Args:
        average (float): Numeric average score

    Returns:
        str: Academic standing description
    """
    if average >= 90:
        return "Dean's List"
    elif average >= 70:
        return "Good Standing"
    elif average >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"


def print_divider(char="=", length=30):
    """
    Helper: print a decorative line.

    Args:
        char (str): Character to use for divider
        length (int): Number of characters to print
    """
    print(char * length)


def display_report(name, scores, average, grade, standing):
    """
    Print the formatted grade report.

    Args:
        name (str): Student name
        scores (list): List of exam scores
        average (float): Calculated average
        grade (str): Letter grade
        standing (str): Academic standing
    """
    print_divider("=", 30)
    print("STUDENT GRADE REPORT")
    print_divider("=", 30)
    print(f"Student: {name}")
    for i, score in enumerate(scores, 1):
        print(f"  Exam {i}: {score}")
    print_divider("-", 30)
    print(f"Average:  {average:.2f}")
    print(f"Grade:    {grade}")
    print(f"Standing: {standing}")
    print_divider("=", 30)


def main():
    """
    Orchestrate the full program.
    """
    print("Grade Calculator")
    print()
    
    # Step 1: Get student info
    name = get_student_name()
    
    # Step 2: Collect scores
    scores = get_exam_scores(3)
    
    # Step 3: Calculate results
    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(average)
    
    # Step 4: Display report
    display_report(name, scores, average, grade, standing)


def test_grade_tracker():
    """
    Run all unit tests using Arrange-Act-Assert pattern.
    """
    print("\n" + "=" * 40)
    print("RUNNING TEST SUITE")
    print("=" * 40 + "\n")
    
    # Test calculate_average - Normal cases
    print("Testing calculate_average():")
    
    # Test 1: Normal case
    scores = [92, 85, 78]
    result = calculate_average(scores)
    expected = 85.0
    print(f"  Test 1 - Normal:     ", end="")
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL (got {result}, expected {expected})")
    
    # Test 2: All same scores
    scores = [80, 80, 80]
    result = calculate_average(scores)
    expected = 80.0
    print(f"  Test 2 - Same:       ", end="")
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL (got {result}, expected {expected})")
    
    # Test 3: Edge - Empty list
    scores = []
    result = calculate_average(scores)
    expected = 0
    print(f"  Test 3 - Empty:      ", end="")
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL (got {result}, expected {expected})")
    
    # Test determine_letter_grade - Normal and boundary cases
    print("\nTesting determine_letter_grade():")
    
    test_cases = [
        (95, "A", "Normal A"),
        (90, "A", "Boundary A"),
        (89.9, "B", "Boundary B"),
        (85, "B", "Normal B"),
        (80, "B", "Boundary B-"),
        (79, "C", "Boundary C"),
        (75, "C", "Normal C"),
        (70, "C", "Boundary C-"),
        (69, "D", "Boundary D"),
        (65, "D", "Normal D"),
        (60, "D", "Boundary D-"),
        (59, "F", "Boundary F"),
        (0, "F", "Zero F"),
    ]
    
    for avg, expected, desc in test_cases:
        result = determine_letter_grade(avg)
        print(f"  Test - {desc:15s} ", end="")
        if result == expected:
            print("PASS")
        else:
            print(f"FAIL (got {result}, expected {expected})")
    
    # Test determine_standing
    print("\nTesting determine_standing():")
    
    standing_cases = [
        (95, "Dean's List", "Normal Dean's"),
        (90, "Dean's List", "Boundary Dean's"),
        (89, "Good Standing", "Boundary Good"),
        (70, "Good Standing", "Boundary Good-"),
        (69, "Academic Probation", "Boundary Probation"),
        (60, "Academic Probation", "Boundary Probation-"),
        (59, "Academic Warning", "Boundary Warning"),
        (0, "Academic Warning", "Zero Warning"),
    ]
    
    for avg, expected, desc in standing_cases:
        result = determine_standing(avg)
        print(f"  Test - {desc:20s} ", end="")
        if result == expected:
            print("PASS")
        else:
            print(f"FAIL (got {result}, expected {expected})")
    
    # Test is_valid_score
    print("\nTesting is_valid_score():")
    
    valid_cases = [
        ("85", True, "Normal valid"),
        ("0", True, "Boundary zero"),
        ("100", True, "Boundary max"),
        ("-5", False, "Negative"),
        ("105", False, "Over max"),
        ("abc", False, "Non-numeric"),
        ("", False, "Empty"),
        ("85.5", False, "Decimal"),
    ]
    
    for score_str, expected, desc in valid_cases:
        result = is_valid_score(score_str)
        print(f"  Test - {desc:15s} ", end="")
        if result == expected:
            print("PASS")
        else:
            print(f"FAIL (got {result}, expected {expected})")
    
    print("\n" + "=" * 40)
    print("TEST SUITE COMPLETE")
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    # Uncomment to run tests:
    # test_grade_tracker()
    main()