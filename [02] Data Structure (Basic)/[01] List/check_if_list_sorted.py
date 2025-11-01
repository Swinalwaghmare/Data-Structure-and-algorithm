# Check if the list is sorted or not

def is_sorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False 
        i = i+1
    return True

def is_sorted_(l):
    i = 1
    for i in len(l):
        if l[i] < l[i-1]:
            return False
        i = i + 1
    return True

def sorted_(l):
    sl = sorted(l)
    if sl == l:
        return True
    else:
        return False 
    
if __name__ == '__main__':
    arr = [10,3,2]
    if sorted_(arr):
        print('Yes')
    else:
        print("No")
