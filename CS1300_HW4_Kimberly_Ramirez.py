# Problem 1: Movie Ticket Pricing
# This program calculates movie ticket prices based on age and showing time

def main():
    # Get age input and validate it's non-negative
    age_input = input("Enter your age: ")
    
    try:
        age = int(age_input)
    except ValueError:
        print("Error: Age must be a valid integer.")
        return
    
    # Validate age is non-negative
    if age < 0:
        print("Error: Age cannot be negative.")
        return
    
    # Get matinee input and convert to boolean using conditional expression
    matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()
    is_matinee = True if matinee_input == "yes" else False
    
    # Determine age group and price using nested if statements
    # Outer level: age group, Inner level: matinee vs regular
    if age < 13:
        age_group = "Child"
        if is_matinee:
            price = 6.00
        else:
            price = 8.00
    elif age <= 17:  # 13-17
        age_group = "Teen"
        if is_matinee:
            price = 7.00
        else:
            price = 10.00
    elif age <= 64:  # 18-64
        age_group = "Adult"
        if is_matinee:
            price = 8.00
        else:
            price = 13.00
    else:  # 65+
        age_group = "Senior"
        if is_matinee:
            price = 6.00
        else:
            price = 7.00
    
    # Display results
    print(f"Age group: {age_group}")
    print(f"Ticket price: ${price:.2f}")

if __name__ == "__main__":
    main()
    
# Problem 2: Input Validator
# This program validates student profile fields and reports all errors at once

def main():
    errors = []  # List to collect all validation errors
    
    # Collect all inputs
    student_id = input("Enter student ID: ").strip()
    full_name = input("Enter full name: ").strip()
    age_input = input("Enter age: ").strip()
    major = input("Enter major: ").strip()
    
    # Validate Student ID
    # Must be exactly 8 characters
    if len(student_id) != 8:
        errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")
    
    # First character must be a letter
    if len(student_id) > 0 and not student_id[0].isalpha():
        errors.append("Student ID must start with a letter")
    
    # Remaining 7 must be digits
    if len(student_id) == 8:
        if not student_id[1:].isdigit():
            errors.append("Student ID must have 7 digits after the first letter")
    
    # Validate Name
    # Not empty after stripping and at least 2 characters
    if len(full_name) == 0:
        errors.append("Name cannot be empty")
    elif len(full_name) < 2:
        errors.append("Name must be at least 2 characters")
    
    # Validate Age
    # Must be valid integer between 16 and 99
    try:
        age = int(age_input)
        if age < 16 or age > 99:
            errors.append("Age must be between 16 and 99")
    except ValueError:
        errors.append("Age must be a valid integer")
        age = None  # Set to None since conversion failed
    
    # Validate Major
    # Must be one of: CS, IT, CE, DS (case-insensitive)
    valid_majors = ["CS", "IT", "CE", "DS"]
    if major.upper() not in valid_majors:
        errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")
    
    # Output results
    if len(errors) == 0:
        # Success case
        print("✓ Profile created successfully!")
        print(f"Student ID: {student_id}")
        print(f"Name: {full_name}")
        print(f"Age: {age}")
        print(f"Major: {major.upper()}")
    else:
        # Error case
        print("✗ Profile has errors:")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    main()

# Problem 3: Campus Café Menu
# A menu-driven ordering system with validation and customization

def main():
    # Display menu
    print("=" * 30)
    print("CAMPUS CAFÉ ORDER SYSTEM")
    print("=" * 30)
    print("1. Coffee - $3.50")
    print("2. Sandwich - $6.00")
    print("3. Salad - $5.50")
    print("4. Combo (Sandwich + Coffee) - $8.00")
    print("5. Exit")
    print("=" * 30)
    
    # Get menu choice
    choice = input("Enter your choice (1-5): ").strip()
    
    # Validate choice
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please select 1-5.")
        return
    
    choice = int(choice)
    
    # Exit option
    if choice == 5:
        print("Goodbye!")
        return
    
    # Variables to store order details
    item_name = ""
    base_price = 0.0
    customization = ""
    
    # Process choice with nested conditionals for customization
    if choice == 1:  # Coffee
        item_name = "Coffee"
        base_price = 3.50
        
        size = input("What size? (small/medium/large): ").strip().lower()
        
        if size == "medium":
            base_price = 4.50
            customization = "Medium"
        elif size == "large":
            base_price = 5.50
            customization = "Large"
        else:
            if size != "small":
                print("Invalid size. Defaulting to Small.")
            customization = "Small"
    
    elif choice == 2:  # Sandwich
        item_name = "Sandwich"
        base_price = 6.00
        
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        
        if cheese == "yes":
            base_price += 0.75
            customization = " + Cheese"
        else:
            customization = ""
    
    elif choice == 3:  # Salad
        item_name = "Salad"
        base_price = 5.50
        
        dressing = input("Dressing choice (ranch/italian/vinaigrette/none): ").strip().lower()
        valid_dressings = ["ranch", "italian", "vinaigrette", "none"]
        
        if dressing in valid_dressings:
            customization = f" + {dressing.capitalize()} dressing" if dressing != "none" else ""
        else:
            print("Invalid dressing. Defaulting to none.")
            customization = ""
    
    elif choice == 4:  # Combo
        item_name = "Combo"
        base_price = 8.00
        
        # Coffee size customization
        size = input("What size coffee? (small/medium/large): ").strip().lower()
        size_extra = 0.0
        size_str = "Small"
        
        if size == "medium":
            size_extra = 1.00
            size_str = "Medium"
        elif size == "large":
            size_extra = 2.00
            size_str = "Large"
        elif size != "small":
            print("Invalid size. Defaulting to Small.")
        
        # Cheese customization
        cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
        cheese_extra = 0.0
        cheese_str = ""
        
        if cheese == "yes":
            cheese_extra = 0.75
            cheese_str = " + Cheese"
        
        base_price = 8.00 + size_extra + cheese_extra
        customization = f" ({size_str} Coffee{cheese_str})"
    
    # Get customer name
    name = input("Enter your name: ").strip()
    while len(name) == 0:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()
    
    # Get quantity with validation
    quantity_input = input("How many? ").strip()
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            print("Quantity must be positive. Defaulting to 1.")
            quantity = 1
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    
    # Calculate totals
    subtotal = base_price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax
    
    # Display receipt
    print("\n" + "=" * 30)
    print("ORDER RECEIPT")
    print("=" * 30)
    print(f"Customer: {name}")
    print(f"Item: {item_name}{customization}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${base_price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("=" * 30)
    print("Thank you for your order!")

if __name__ == "__main__":
    main()