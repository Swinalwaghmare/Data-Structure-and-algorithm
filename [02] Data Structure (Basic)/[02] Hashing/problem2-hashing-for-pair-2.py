# Hashing for pair - 2
# Difficulty: EasyAccuracy: 68.08%Submissions: 26K+Points: 2
# You are given an array of integers and an integer sum. You need to find if two numbers in the array exists that have sum equal to the given sum.

# Example 1:

# Input:
# N = 10
# arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# sum = 14

# Output: 
# 1

# Explanation: 
# there exists a pair which 
# gives sum as 14 example 
# (4,10),(5,9) etc.
# Example 2:

# Input:
# N = 4
# arr[] ={4, 3, 5, 6}
# sum = 12

# Output: 
# 0

# Explanation: 
# there does not exist any
# such pair which gives sum as 12.


from asyncio import TaskGroup


def sum_exist(arr,target):
    seen = set()
    count = 0
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            count += 1
        seen.add(arr[i])
    if count > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    arr = [4, 3, 5, 6]
    target = 12
    print(sum_exist(arr, target))
