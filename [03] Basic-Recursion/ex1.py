def function1(n):
    if n == 0:
        return
    print("GFG")
    function1(n-1)

if __name__ == '__main__':
    function1(5)                