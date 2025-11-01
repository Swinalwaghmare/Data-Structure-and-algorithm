def function(n):
    if n == 0:
        return
    print(n)
    function(n-1)
    print(n)

if __name__ == '__main__':
    function(3)