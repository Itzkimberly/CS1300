# ============================================================
# EXERCISE 1 — Display the Menu
# Pattern practiced: for loop with range()
# ============================================================

# Starter data (copy this for each exercise)
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]
order_descriptions = []
order_prices = []
order_sizes = []

pizza_order = input("Order a pizza(yes/no)")
# ----- EXERCISE 1 CODE -----
if pizza_order.lower() == "yes":
    while True:
        print("=" * 40)
        print("PIZZA SIZES")
        print("=" * 40)

        for i in range(len(sizes)):
            print(f"{i + 1}. {sizes[i]:<15} ${size_prices[i]:>5.2f}")

        print("=" * 40)

        # EXERCISE 2
        while True:
            try:
                size_choice = int(input("Choose a size (1-4):")) - 1
                if size_choice == 0:
                    base_price = 6.99
                    size = "Personal"
                    break
                elif size_choice == 1:
                    base_price = 9.99
                    size = "Medium"
                    break
                elif size_choice == 2:
                    base_price = 12.99
                    size = "Large"
                    break
                elif size_choice == 3:
                    base_price = 16.99
                    size = "Party"
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a number.")
        order_sizes.append(size_choice)
        


        # Exercise 3
        selected_toppings = []  # Reset for each pizza!

        print("\nAvailable toppings ($1.50 each):")
        for i in range(len(topping_names)):
            print(f"  {i + 1}. {topping_names[i]}")

        # Topping selection loop (sentinel: "done")
        while True:
            topping_input = input("\nAdd topping # (or 'done'): ").strip().lower()
    
            if topping_input == "done":
                break  # Sentinel value - exit loop
    
            try:
                topping_num = int(topping_input) - 1  # Convert to 0-based
        
            # Check if valid topping number
                if topping_num < 0 or topping_num >= len(topping_names):
                    print(f"Choose 1-{len(topping_names)}.")
                    continue  # Skip back to prompt
        
                topping_name = topping_names[topping_num]
        
            # Check for duplicates
                if topping_name in selected_toppings:
                    print(f"Already added {topping_name}!")
                    continue  # Skip back to prompt
        
            # Add the topping
                selected_toppings.append(topping_name)
                print(f"  ✓ Added {topping_name}")
        
            except ValueError:
                print("Please enter a number or 'done'.")
                continue  # Skip back to prompt

        # Exercise 4
        order_description = ""
        toppings = ""
        price = base_price + (len(selected_toppings) * 1.5)
        for i in range (len(selected_toppings)):
            toppings += selected_toppings[i-1]
            if i < len(selected_toppings) - 1:
                toppings += ", "
        if toppings == "":
            toppings = "Cheese"
        order_prices.append(price)
        order_descriptions.append(size + " " + toppings)

        # Excerise 5
        while True:
            another = input("\nOrder another pizza? (yes/no): ").strip().lower()
    
            if another in ["yes", "y"]:
                break  # Continue outer loop
            elif another in ["no", "n"]:
                break  # Will exit outer loop
            else:
                print("Please enter 'yes' or 'no'.")
                continue
    
        if another in ["no", "n"]:
            break  # Exit ordering loop

    # Exercise 8
    attempts = 0
    discount = 0.00
    while True:
        discount_code = input("Enter discount code ('none' to skip): ")
        if discount_code == "STUDENT10":
            discount = 0.10
            break
        elif discount_code == "HALFOFF":
            discount = 0.50
            break
        elif discount_code == "none":
            print("No discount applied.")
            break
        else:
            print("Code invalid.")
        attempts +=1
        if attempts == 3:
            print("No discount applied.")
            break
    

        # Exercise 6
    print("=" * 40)
    print("\t YOUR ORDER RECEIPT")
    print("=" * 40)
    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i-1]}")
        print(f"${order_prices[i]:>25.2f}")
    print("-" * 40)
    subtotal = 0
    discount_total = 0.00
    for order_price in order_prices:
        subtotal += order_price
    if not discount == 0.00:
        discount_total = subtotal * discount
    tax = subtotal * .07
    total = subtotal + tax - discount_total
    print(f"Subtotal:\t {subtotal:>25.2f}")
    print(f"Tax:\t {tax:>25.2f}")
    if not discount == 0.00:
        print(f"Discount:\t {discount_total:>25.2f}")
    print(f"Total:\t {total:>25.2f}")
    print("=" * 40)
    print("Thank you for your order!")

    # Exercise 7 After printing receipt
    max_price = -1
    max_index = 0

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    print(f"\nMost expensive: {order_descriptions[max_index]} (${max_price:.2f})")

    # Stretch: Also find cheapest
    min_price = float('inf')
    min_index = 0
    for i in range(len(order_prices)):
        if order_prices[i] < min_price:
            min_price = order_prices[i]
            min_index = i
    print(f"Cheapest: {order_descriptions[min_index]} (${min_price:.2f})")

    # Exercise 9


    # After receipt, add:
    print("\n" + "-" * 40)
    print("         ORDER SUMMARY BY SIZE")
    print("-" * 40)

    size_counts = [0, 0, 0, 0]  # Counter for each size

    for size_idx in order_sizes:
        size_counts[size_idx] += 1

    for i in range(len(sizes)):
        if size_counts[i] > 0:
            print(f"  {sizes[i]:<20} x{size_counts[i]}")

    # Stretch: Average price
    avg_price = sum(order_prices) / len(order_prices)
    print(f"\n  Average price per pizza: ${avg_price:.2f}")
else:
    print("No pizzas ordered.")