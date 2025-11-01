# Reversed a given list
def reversed_list(l):
   s = 0
   e = len(l)-1
   while s < e :
       l[s],l[e] = l[e], l[s]
       s = s + 1
       e = e - 1

if __name__ == '__main__':
    l = [10,20,30,40]
    #result = reversed(l)
    reversed_list(l)
    print(l)
    