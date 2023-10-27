def generate_fibonacci(n):
    fib_sequence = [0, 1]

    if n <= 0:
        return []

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

try:
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci Sequence:")
        print(fibonacci_sequence)
except ValueError:
    print("Please enter a valid positive integer for the number of terms.")

