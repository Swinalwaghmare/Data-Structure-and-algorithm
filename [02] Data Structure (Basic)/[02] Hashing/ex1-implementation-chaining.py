# Implementation of chaining in python
class Hash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(self.BUCKET)]

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)
    
    def remove(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
           self.table[i].remove(x)
        else:
            pass
        
    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

if __name__ == '__main__':
    bucket_size = int(input('Enter bucket size: '))
    obj = Hash(bucket_size)
    x = int(input('Enter a number: '))
    obj.insert(x)
    x = int(input('Enter a number: '))
    obj.insert(x)
    x = int(input('Enter a number: '))
    obj.insert(x)
    x = int(input('Enter a number: '))
    obj.insert(x)
    x = int(input('Enter a number: '))
    obj.insert(x)
    x = int(input("Enter a serch number: "))
    print(obj.search(x))
    x = int(input("Enter a remove number: "))
    obj.remove(x)
    x = int(input("Enter a serch number: "))
    print(obj.search(x))