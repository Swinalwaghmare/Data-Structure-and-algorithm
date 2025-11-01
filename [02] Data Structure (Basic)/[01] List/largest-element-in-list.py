# Largest element in the list
# for every element, check if it is the largest
# [10, 20, 5, 50]

'''
 def getmax(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None
'''

## Efficient solution

def getmax(l):
    
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
                
        return res
    
if __name__ == '__main__':
    l = [10, 20, 5, 50]
    # l = []
    result = getmax(l)
    print(result)
    
# Output
# 50
# None