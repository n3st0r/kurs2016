
def persistence(n: int) -> int:
    i = 0

    def int_to_list(m):
        lista = []
        for n in str(m):
            if n.isdigit():
                lista.append(int(n))
        return lista

    def multiplication(lista: list):

        if len(lista) == 1:
            return lista.pop(0)

        wynik = lista.pop(0)
        while len(lista) > 0:
            wynik = wynik * lista.pop(0)

        return wynik

    while len(str(n)) > 1:
        i += 1
        n = multiplication(int_to_list(n))

    return i


if __name__ == '__main__':
    print(persistence(39))
    print(persistence(4))
    print(persistence(25))
    print(persistence(999))
