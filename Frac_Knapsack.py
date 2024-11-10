from fractions import Fraction

# Function to solve the fractional knapsack problem
def fractional_knapsack(capacity, weights, profits):
    n = len(weights)
    # Calculate profit-to-weight ratio and sort items by it in descending order
    items = sorted([(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)], reverse=True,
                   key=lambda x: x[0])

    total_value = 0
    proportions = []

    for ratio, weight, profit in items:
        if capacity == 0:
            break

        # Take as much as possible of the current item
        if weight <= capacity:
            capacity -= weight
            total_value += profit
            proportions.append(Fraction(1))  # Full item taken
        else:
            fraction = Fraction(capacity, weight)  # Fraction of the item taken
            total_value += profit * float(fraction)
            proportions.append(fraction)
            capacity = 0  # Knapsack is now full

    return proportions, total_value


# Input from user
capacity = int(input("Enter capacity of knapsack: "))
n = int(input("Enter the number of items: "))
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
profits = list(map(int, input("Enter the profit of the items separated by space: ").split()))

# Solving the problem
proportions, total_value = fractional_knapsack(capacity, weights, profits)

# Output the results
print("Proportions of items taken (as reduced fractions):")
for i, fraction in enumerate(proportions):
    print(f"Item {i + 1}: {fraction}")

print(f"Total value of the knapsack: {total_value:.2f}")
