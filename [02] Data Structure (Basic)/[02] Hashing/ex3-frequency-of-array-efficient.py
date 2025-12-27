def count_freq(arr, n):
    hmp = dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]] += 1
        else:
            hmp[arr[i]] = 1

    for x in hmp:
        print(x, " ", hmp[x])

if __name__ == '__main__':
    arr = [10, 12, 10, 15, 10, 20, 12, 12]
    n = len(arr)
    count_freq(arr, n)