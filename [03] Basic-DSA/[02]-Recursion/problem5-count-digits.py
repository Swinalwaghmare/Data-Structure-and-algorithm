# Count Digits in a Number
# You are given a number n. You need to find the count of digits in n.

# Examples :

# Input: n = 1
# Output: 1
# Explanation: Number of digit in 1 is 1.
# Input: n = 99999
# Output: 5
# Explanation: Number of digit in 99999 is 5
# Constraints:
# 1 ≤ n ≤ 109

def function(n):
    if n < 10:
        return 1
    return 1 + function(n//10)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = function(n)
    print(f"Number of digit in {n} is {result}")