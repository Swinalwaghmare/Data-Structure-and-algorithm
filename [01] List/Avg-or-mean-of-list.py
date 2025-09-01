# Given a list of numbers, the task is to find average of that list.

class Solution:
    
    # basic app
    def basic_app(self,l):
        """
        Calculate the average of a list of numbers.

        Parameters:
        - numbers (list): A list of numerical values for which the average will be calculated.

        Returns:
        - float: The average value of the input list.
        """
        sum = 0
        for i in l:
            sum += i
        n = len(l)
        return sum/n
    
    def adv_approach(self,l):
        return sum(l)/len(l)

if __name__ == '__main__':
    obj = Solution()
    l = [10, 20, 30, 40]
    # print(obj.basic_app(l))
    print(obj.adv_approach(l))
        
#Output :
#25.0
