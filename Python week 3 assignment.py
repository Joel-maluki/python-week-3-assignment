# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it's 20% or higher.
    :param price: Original price of the item
    :param discount_percent: Discount percentage
    :return: Final price after applying the discount or the original price
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if discount_percentage >= 20:
    print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")