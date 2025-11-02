# Example 1:

# Input:
# n = 100
# Output: 0
# Example 2:

# Input:
# n = 101
# Output: 1

class Solution:
    def reverse_num(self, n, rev=0):
        if n == 0:
            return rev
        last_digit = n % 10
        rev = rev * 10 + last_digit
        
        return self.reverse_num(n // 10, rev)
        
    def isPalin(self,N):
        if N == self.reverse_num(N):
            return 1
        else:
            return 0

if __name__ == '__main__':
    obj = Solution()
    N = int(input("Enter a Number: "))
    result = obj.isPalin(N)
    print(result)