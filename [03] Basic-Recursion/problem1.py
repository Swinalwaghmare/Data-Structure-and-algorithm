# You are given a number n. You need to recursively find the nth term of the series S that is given by:
# S(n) = n+ n*(S(n-1)) and S(0) = 1

# Example 1:
# Input:
# n = 2
# Output: 6

# Example 2:
# Input:
# n = 3
# Output: 21

def function(n):
    if n == 0:
        return 1
    return n + n * function(n-1)

if __name__ == '__main__':
    print(function(3))