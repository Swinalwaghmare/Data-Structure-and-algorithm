from unittest import result


def function(str, start, end):
    if start >= end:
        return True
    return (str[start] == str[end] and function(str, start+1, end-1))


if __name__ == '__main__':
    str = input("Enter string:")
    start = 0
    end = len(str)-1
    result = function(str, start, end)
    print(f"{str} is palindrom {result}")