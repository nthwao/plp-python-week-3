def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output the result
    if final_price < original_price:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
