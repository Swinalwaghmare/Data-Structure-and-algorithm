# Recursively Sum N Numbers
# You are given a number n. You need to recursively sum the numbers from 1 to n and return the sum.

# Example 1:

# Input:
# n = 5
# Output: 15
# Example 2:

# Input:
# n = 4
# Output: 10

def function(n):
    if n <= 1:
        return n
    return n + function(n - 1)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = function(n)
    print(result)