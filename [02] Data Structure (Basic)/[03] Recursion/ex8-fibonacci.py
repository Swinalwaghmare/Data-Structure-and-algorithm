def function(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return function(n-1) + function(n-2)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = function(n)
    print(f"Fibonacci number of {n} is {result}")