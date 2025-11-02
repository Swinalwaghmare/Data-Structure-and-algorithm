# array = [1, 2, 1, 2, 4]
def function(arr, ele):
    count = 0
    for i in arr:
        if i == ele:
            count += 1
    
    return count

if __name__ == '__main__':
    arr = [int(item) for item in input("Enter Number by spaces").split()]
    ele = int(input("Enter a number: "))
    result = function(arr, ele)
    print(result)