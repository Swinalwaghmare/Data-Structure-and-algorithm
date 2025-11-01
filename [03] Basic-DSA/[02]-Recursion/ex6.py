def function(n):
    if n <= 0: # n<=0 to handle the negative numbers
        return
    print(n, end=" ")
    function(n-1)

if __name__ == '__main__':
    function(5)