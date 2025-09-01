class Solution:
    def __init__(self,n):
        self.n = n

    def sumofnaturalnums(self):
        print(self.n * (self.n + 1)//2)

        
if __name__ == '__main__':
    n = int(input("Enter a Number: "))
    obj = Solution(n)
    obj.sumofnaturalnums()