# Without recursion
def fibonacci_iterative(n1, n2, terms):
    result = [n1, n2]
    while terms > 2:
        c = n1 + n2
        result.append(c)
        n1 = n2
        n2 = c
        terms -= 1
    return result

# With recursion
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Get user input
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n_terms = int(input('Enter the number of terms: '))

# Display result without recursion
print("Fibonacci sequence without recursion:")
iterative_result = fibonacci_iterative(n1, n2, n_terms)
print(" ".join(map(str, iterative_result)))

# Display result with recursion
print("\nFibonacci sequence with recursion (starting from 0, 1):")
recursive_result = [fibonacci_recursive(i) for i in range(n_terms)]
print(" ".join(map(str, recursive_result)))