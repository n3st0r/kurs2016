
def xo(s):
    char_x = 0
    char_o = 0
    for char in s:
        if str(char).lower() == 'x':
            char_x += 1
        elif str(char).lower() == 'o':
            char_o += 1
    print(char_o)
    print(char_x)
    if char_x == char_o:
        return True
    else:
        return False


if __name__ == '__main__':
    print(xo('xo'))
    print(xo('xo0'))
    print(xo('xxxoo'))
    print(xo('xXXOoo'))
    print(not xo('xxxoo'))
