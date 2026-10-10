
total = 0
item_count = 0

while True:
    user_input = input("Enter item price (or 'q' to quit): ")

    if user_input.lower() == "q":
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price
        item_count += 1

    except ValueError as e:
        print("Error:", e)

print("\nShopping Cart Summary")
print("Total valid items:", item_count)
print("Final bill:", total)
