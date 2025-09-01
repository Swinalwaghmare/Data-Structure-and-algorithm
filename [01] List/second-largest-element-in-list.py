# second larget element in list 
# input : [10, 5, 8, 20]
# output : [10]

def getSecMax(arr):
    if len(arr) <= 1:
        return None
    lar = max(arr)
    slar = None
    for x in arr:
        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(slar, x)
    return slar

def get_Sec_Max(arr):
    if len(arr) <= 1:
        return None
    lar = arr[0]
    slar = -1
    for x in arr[1:]:
        if x > lar:
            slar = arr[0]
            lar = x
        elif x != lar:
            if slar==None or slar<x:
                slar = x
    return slar

if __name__ == '__main__':
    arr = [20, 10, 20, 8, 12]
    result = get_Sec_Max(arr)
    print(result)
    
# Output
# 12