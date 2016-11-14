l = [1, 2]

try:
    b = l[2]
except IndexError as e:
    b = 0
    print('Wystąpił błąd: ', e)

print(b)