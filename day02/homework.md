Zadanie dowowe :)

# 1. Stworzyc nowy modul pythonowy (plik) "kolo.py".

Napisz funkcję, która policzy obwód koła. Parametrem funkcji powinien być "promien". Funkcja ma zwrócić obwód koła.

Napisz funkcję, która policzy pole koła. Parametrem funkcji powinien być "promien". Funkcja ma zwrócić pole koła. 

Możesz użyc jako pi wartości 3.14

# 2. Stworzyć nowy moduł pythonowy (plik) o nazwie "program1.py".

Zaimportuj moduł "kolo.py"

Stwórz pętlę, która dla wartości od 1 do 20 policzy pole i obwód koła, zakładając, że wartość w pętli to promień koła.
Do obliczeń użyj funkcji z modułu "kolo.py". Wyniki obliczeń wydrukuj w następujący sposób:

promien:  1 obwod:  6.283185307179586 pole:  3.141592653589793

dla każdej z wartości w pętli. 

# 3. Zmień kolo.py tak, aby używać pi z modułu math.
Więcej o module math tutaj:
https://docs.python.org/3.5/library/math.html#constants

# 4. użyj zaokrąglenia
użyj zaokrąglenia, aby wyświetlać tylko 2 miejsca po przecinku. 
https://docs.python.org/3/library/functions.html#round

Trudniejsze:

# 5. 
Postaraj się sformatować wynik tak, aby wartości liczbowe były wyrównane do prawej, mniej więcej tak:

promien:    1 obwod:     6.28 pole:     3.14
...
promien:   19 obwod:   119.38 pole:  1134.11

Sposobów jest kilka, a oto podpowiedzi/przypomnienia:
funkcja rjust():
https://docs.python.org/3.5/library/stdtypes.html#str.rjust

str.format():
https://docs.python.org/3/library/stdtypes.html#str.format
i przykłady:
https://docs.python.org/3/library/string.html#format-examples