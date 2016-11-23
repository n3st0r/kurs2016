Praca domowa:)

1. Napisz klasę "Prostokat". Niech klasa w konstruktorze przyjmie 2 parametry: "a" i "b",
które będą reprezentowały długość boku a i boku b w prostokącie. 

2. Napisz magiczną metodę (dunder) `__str__()` tak, aby zwracała stringa zawierającego:
"Prostokąt - bok a: 1, bok b: 2" 
gdzie wartości 1 i 2 będą pobrane z obiektu. Przetestuj tworząc obiekt z różnymi wartościami boków "a" i "b",
a następnie wydrukuj instancję obiektu, przekazując ją do funkcji print(). 

3. Dopisz do klasy prostokąt metodę `pole_prostokata()`, która policzy i zwróci pole prostokąta.

4. Dopisz do klasy prostokąt metodę `obwod_prostokata()`, która policzy i zwróci obwód prostokąta. 

5. Dopisz metodę `czy_kwadrat()` która zwróci bool (True lub False), w zależności od tego, czy prostokąt jest kwadratem. 

6. Dopisz metodę `boki()` która zwróci krotkę z długością boku "a"  i "b"

7. Jeśli jeszcze tego nie zrobiłeś, zmień pola obiektu "a" i "b", na pola prywatne. (`_`)

8. Dopisz metodę `opis()` która zwróci stringa z opisem obiektu zawierającego informacje o polu, obwodzie
i tym czy jest prostokątem. Przykładowy string z wartością:
"Prostokąt - bok a: 1, bok b: 2, pole: 2, obód: 6, czy kwadrat: Nie"
"Prostokąt - bok a: 3, bok b: 3, pole: 9, obód: 12, czy kwadrat: Tak"

Uwaga. Nie używaj funkcji `__str__()`. możesz użyć metod pole_prostokata() i obwód prostokata() aby obliczyć te wartości.
