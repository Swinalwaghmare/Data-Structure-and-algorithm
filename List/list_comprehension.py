## Finding a list of all the numbers smaller than x 
## getting two list where first list is odd and second list is even

class Solution:
    
    def get_n_small_x(self,arr,x):
        return [i for i in arr if i<x ]
    
    def get_odd_even_numbers(self, x):
        even = [i for i in range(x) if i%2==0]
        odd = [i for i in range(x) if i%2!=0]
        return even , odd
    
    
if __name__ == '__main__':
    obj = Solution()
    # print(obj.get_n_small_x(arr=[1,2,3,4,5],x=3))
    # Output [1, 2]
    # print(obj.get_odd_even_numbers(x=11))
    # output ([0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9])