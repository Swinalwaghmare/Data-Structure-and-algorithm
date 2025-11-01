# Sum of Digits of a Number
# Difficulty: BasicAccuracy: 73.02%Submissions: 73K+Points: 1
# You are given a number n. You need to find the sum of digits of n.

# Examples :

# Input: n = 1
# Output: 1
# Explanation: Sum of digit of 1 is 1.
# Input: n = 99999
# Output: 45
# Explanation: Sum of digit of 99999 is 45.
# Constraints:
# 1 ≤ n ≤ 107

import fnmatch
from unittest import result


def function(n):
    if n < 10:
        return n
    return function(n//10) + n % 10

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    result = function(n)
    print(f"Sum of digit of {n} is {result}")