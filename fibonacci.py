def fibonacci(n):
    fibo_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib0_series

n = int(input("Enter the number of terms: "))
result = fibonacci(n)
print(result)
