# Seperate even and oddd values from list
# input : l = [10, 41, 30, 15, 80]
# outpur : even = [10, 30, 80]
#          odd = [41, 15]

class Solution:
    
    def sep_eve_odd(self, arr):
        """
        Separates a list of integers into two lists: 
        one containing even numbers and the other containing odd numbers.
    
        Args:
            arr (list): The input list of integers to be separated.

        Returns:
            tuple of lists: A tuple containing two lists:
            1. List of even numbers from the input list.
            2. List of odd numbers from the input list.
        """
        even = []
        odd = []
        for i in arr:
            if i % 2 == 0:
               even.append(i)
            else:
                odd.append(i) 
        return even , odd
    
    
if __name__ == '__main__':
    obj = Solution()
    arr = [10, 41, 30, 15, 80]
    print(obj.sep_eve_odd(arr))
    
# Output
# ([10, 30, 80], [41, 15])