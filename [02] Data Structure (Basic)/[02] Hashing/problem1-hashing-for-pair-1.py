# Hashing for pair - 1
# You are given an array of distinct integers and a sum. Check if there's a pair with the given sum in the array.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], sum = 14
# Output: 1
# Explanation: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and sum = 14.  There is a pair [4, 10] with sum 14.
# Input: arr[] = [2, 5], sum = 10
# Output: 0
# Explanation: arr[]  = [2, 5] and sum = 10. There is no pair with sum 10.


def sumExists(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return 1
        seen.add(num)
    return 0    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 14
    print(sumExists(arr, target))