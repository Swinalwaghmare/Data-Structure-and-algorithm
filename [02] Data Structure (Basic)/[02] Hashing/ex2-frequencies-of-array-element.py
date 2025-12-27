def function(arr, n):
    for i in range(n):
        flag = False
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
        if flag == True:
            continue
        freq = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                freq += 1
        print(arr[i], freq)

if __name__ == '__main__':
    arr = [10, 12, 10, 15, 10, 20, 12, 12]
    n = len(arr)
    function(arr, n)