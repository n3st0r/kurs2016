
try:
    f = open('plik, którego nie ma')
except FileNotFoundError:
    print('Pliku nie ma')
else:
    c= f.read()
    print(c)
