def function(n):
    if n == 0:
        return
    function(n // 2)
    print(n % 2)

if __name__ == '__main__':
    function(13)