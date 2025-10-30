# Get smaller element from the list
# Input : l = [8, 100, 20, 40, 3, 7]
# Condition : x = 10
# output : [8, 3, 7]

class Solution:
    def get_smaller_ele(self,arr,x):
        list = []
        for i in arr:
            if i < x:
                list.append(i)
            
        return list
    
    
if __name__ == '__main__':
    obj = Solution()
    arr = [100, 20, 40, 60, 80, 200]
    print(obj.get_smaller_ele(arr=arr,x=60))
    
# Output
# [20, 40]