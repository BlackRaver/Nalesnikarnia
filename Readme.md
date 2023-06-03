Struktura aplikacji
Aplikacja opiera się o wzorzec projektrowy typu "builder"
-Funkcja main inicjuje zmienne globalne w których przechowujemy składniki i opcje naleśników w Enumach (sprawia że kod jest elastyczny ponieważ nie musimy operować na indexach)
-Zostaje wyświetlone proste menu gdzie wprowadzając odpowiedni skrót możemy wybrać jakiego chcemy naleśnika
-W zależności od naszego wyboru obiekt klasy obsluga.py przypisze do siebie odpowiedni builder który stwoży wybrany przez nas naleźnik
-W trakcie procesu tworzenia naleśnika wybrany przez nas builder twoży obiekt nalesnik za pomocą klasy Nalesnik poprzez podsyłanie odpowiadających wybranemu naleśnikowi parametrów (rodzaj ciasta, farsz, polewa)

Scenariusze testów
-Test1 
Sprawdza poprawność działania klasy Nalesnik.
klasa ta ma za zadanie twożyć naleśnik za pomocą własnych metod z wykożystaniem otrzymywanych parametrów.
Test ten sprawdza wartosci atrybutów: [nazwa,placek,farsz,polewa]

-Test2 
Sprawdza poprawnośc zachowania metod [wypelnij,polejSosem] w sytuacji otrzymania pustych wartości (naleśnik nie ma wypełnienia i polewy)

-Test3 
Sprawdza poprawność działania klasy Obsluga poprzez spradzenie poprawnosci wykorzystywanego przez klase Obsluga buildera nalesnika.
Nastepnie jest wykonane sprawdzenie poprawdności utwożonego przez  builder NalesnikZSerem naleśnika przez przyrównanie wartosci atrybutów do stwożonego przez nas obiektu placek klasy NalesnikZSerem.

-Test4
Jest powtórzeniem Testu3 tylko że wykostuje builder klasy PancakeKlonowy

Wykorzystane narzędzia i technologie:
-Python
biblioteki
   -time
   -unittest
  
-VisualStudioCode
pluginy
  -Python
  -Pylance

