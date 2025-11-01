# Print Array Elements Using Recursion
# You are given an array arr of size n. You need to print the array elements from start to end using given recursive function.

# Example 1:
# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 1 2 3 4 5

# Example 2:
# Input:
# n = 4
# arr[] = {5,4,2,1}
# Output: 5 4 2 1

def function(arr,n):
    if n == 0:
        return
    function(arr,n-1)
    print(arr[n-1], end=" ")

if __name__ == '__main__':
    arr = [5,4,2,1]
    n = 4
    function(arr, n)