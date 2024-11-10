def knapsack_01(capacity, weights, profits):
    n = len(weights)
    # Create a 2D DP array to store the maximum profit for each capacity and item count
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Choose max of including the item or excluding it
                dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The bottom-right cell has the max profit


# Input from user
capacity = int(input("Enter capacity of knapsack: "))
n = int(input("Enter the number of items: "))
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
profits = list(map(int, input("Enter the profit of the items separated by space: ").split()))

# Solving the problem
max_profit = knapsack_01(capacity, weights, profits)

# Output the result
print(f"Maximum Profit: {max_profit}")
