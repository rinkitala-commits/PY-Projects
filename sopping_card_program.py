foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of the food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    foods.append(food)

    while True:
        try:
            price = float(input(f"Enter the price of {food}: $ "))
            if price < 0:
                print("Price must be a positive number. Please try again.")
            else:
                prices.append(price)
                total += price
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("\n---Your Shopping Cart ---")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

print(f"\nTotal: ${total:.2f}")