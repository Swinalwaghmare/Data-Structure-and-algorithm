# Factorial of n where n >= 0
def function(n):
    if n == 0:
        return 1
    return n * function(n-1)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = function(n)
    print(f"Factorial of {n} is {result}")