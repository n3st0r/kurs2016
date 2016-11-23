
try:
    f = open('a')
    c = f.read()
    liczba = int(c)
except FileNotFoundError:
    print('Pliku nie ma')
except ValueError:
    print('Błędy w pliku')
    raise
else:
    c= f.read()
    print(c)
finally:
    f.close()
    print('finally')
