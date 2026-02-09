# Problem 1: User Profile Generator
"""
User Profile Generator
CS1300 HW2 - Problem 1
"""

# Get user input - these are PROMPTS (questions), not answers
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")
hobby = input("Enter your favorite hobby: ")

# Convert names to proper title case
first_name = first_name.title()
last_name = last_name.title()

# Calculate age (current year is 2026)
age = 2026 - int(birth_year)

# Create decorative border
border = "=" * 30

# Display formatted profile card
print(f"\n{border}")
print("       USER PROFILE CARD")
print(f"{border}")
print(f"Name:  {first_name} {last_name}")
print(f"Age:   {age}")
print(f"Hobby: {hobby}")
print(f"{border}")
print("Thank you for creating your profile!")

# Problem 2: Text Analyzer
"""
Text Analyzer
CS1300 HW2 - Problem 2
"""

# Get input from user
sentence = input("Enter a sentence: ")

# Calculate statistics
total_with_spaces = len(sentence)
total_without_spaces = len(sentence.replace(" ", ""))
word_count = len(sentence.split())
vowel_count = sum(1 for char in sentence.lower() if char in "aeiou")
uppercase_version = sentence.upper()
lowercase_version = sentence.lower()
reversed_sentence = sentence[::-1]
starts_with_capital = sentence[0].isupper() if sentence else False
ends_with_punctuation = sentence[-1] in ".!?" if sentence else False

# Display results
print(f"\n{'='*20} TEXT ANALYZER {'='*20}")
print("-- Analysis Results --")
print(f"Total characters (with spaces):  {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words:                 {word_count}")
print(f"Number of vowels:                {vowel_count}")
print(f"\nUppercase version:               {uppercase_version}")
print(f"Lowercase version:               {lowercase_version}")
print(f"Reversed:                        {reversed_sentence}")
print(f"\nStarts with capital:             {'Yes' if starts_with_capital else 'No'}")
print(f"Ends with punctuation:           {'Yes' if ends_with_punctuation else 'No'}")

# Bonus: Palindrome Checker
"""
Palindrome Checker - Bonus
CS1300 HW2 - Bonus
"""

def is_palindrome(text):
    """
    Check if text is a palindrome (case-insensitive, ignores spaces).
    """
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    
    # Compare with reverse
    return cleaned == cleaned[::-1]


# Test the function
test_cases = [
    "Racecar",
    "A man a plan a canal Panama",
    "Hello",
    "Was it a car or a cat I saw"
]

print("=" * 40)
print("       PALINDROME CHECKER")
print("=" * 40)

for test in test_cases:
    result = "Palindrome" if is_palindrome(test) else "Not a palindrome"
    print(f'"{test}"')
    print(f"  → {result}\n")

# Interactive version
user_input = input("Enter a word or phrase to check: ")
if is_palindrome(user_input):
    print("✓ This IS a palindrome!")
else:
    print("✗ This is NOT a palindrome.")