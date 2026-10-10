
prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        if price == 0:
            print("Invalid price: Price must be positive")
            continue

        total += price

    except TypeError as e:
        print("Type Error:", e)

    except ValueError as e:
        print("Value Error:", e)

    else:
        print("Running total:", total)

print("Final total:", total)
