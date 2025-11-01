# Left rotate a list by one
# input : [10, 20, 30, 40]
# output : [20, 30, 40, 10]

# using indexing and slicing
def rotate1_(arr):
    arr = arr[1:] + arr[0:1]
    return arr

# using append method
def rotate2_(arr):
    arr.append(arr.pop(0))
    return arr

# Our own logic
def rotate3_(arr):
    temp = []
    res = 1
    for i in range(1,len(arr)):
        temp.append(arr[i])
    
    temp.append(arr[0])
    return temp

def rotate_by_one(arr):
    n = len(arr)
    x = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = x

if __name__ == '__main__':
    arr = [10, 20, 30, 40]
    #print(rotate2_(arr=arr))
    #print(rotate3_(arr=arr))
    rotate_by_one(arr)
    print(arr)