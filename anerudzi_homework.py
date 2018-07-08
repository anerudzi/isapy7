print("Uruchom odpowiedni program - wybierz od 1 do 10, zgodnie z ponizsza lista:")
print("1 Program do przeliczania stopni Celsjusza na Fahrenheita")
print("2 Program do przeliczania stopni Fahrenheita na Celsjusza")
print("3 Program do obliczania pola powierzchni kola o zadanym promieniu")
print("4 Program ktory poda pierwsza i ostatnia cyfre podanej liczby")
print("5 Program ktory rysuje prostokat o zadanych rozmiarach")
print("6 Program do przeliczania liczby zapisanej w formacie binarnym na system dziesietny")
print("7 Program do rozpoznawania czy podane liczba jest parzysta czy nie.")
print("8 Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7")
print("9 Pogram do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7")
print("10 Program do sprawdzania czy podany rok jest rokiem przestepnym")
wybrany_program = int(input("       Wybieram program = "))

if wybrany_program == 1:
    print("Wybrano 1. Program do przeliczania stopni Celsjusza na Fahrenheita")
    print("Aby zamienic stopnie Celsjusza na stopnie Fahrenheita nalezy skorzystac ze wzoru: F = 9/5 * C + 32")
    Cel = int(input("Podaj wartosc temperatury w stopniach Celsjusza: "))
    Fah = 9 / 5 * Cel + 32
    print ("Wartosc temperatury w Fahrenheitach wynosi: ", Fah, "F")

elif wybrany_program == 2:
    print("Wybrano 2 Program do przeliczania stopni Fahrenheita na Celsjusza")
    print("Aby zamienic stopnie Celsjusza na stopnie Fahrenheita nalezy skorzystac ze wzoru: F = 5/9 * C - 32")
    Fah = int(input("Podaj wartosc temperatury w stopniach Fahrenheita: "))
    Cel = 5/9 * Fah - 32
    print ("Wartosc temperatury w Celsjuszach wynosi: ", Cel, "C")

elif wybrany_program == 3:
    print("Wybrano 3 Program do obliczania pola powierzchni kola o zadanym promieniu")
    r = int(input("Promien kola = "))
    print("Pole kola wynosi = ", 3.14*r*r)

elif wybrany_program == 4:
    print("Wybrano 4 Program ktory poda pierwsza i ostatnia cyfre podanej liczby")
    liczba = input("Podaj liczbe = ")
    print ("Pierwsza cyfra podanej liczby to = ", liczba[0])
    print("Ostatnia cyfra podanej liczby to = ", liczba[-1])

elif wybrany_program == 5:
    print("Wybrano 5 Program ktory rysuje prostokat o zadanych rozmiarach")
    a=int(input("Podaj wymiar a= "))
    b=int(input("Podaj wymiar b= "))
    print("+", "-"* (a-2), "+")
    while b>0:
        print("|", " " * (a-2), "|")
        b -=1
    print("+", "-" * (a - 2), "+")

elif wybrany_program == 6:
    print("Wybrano 6 Program do przeliczania liczby zapisanej w formacie binarnym na system dziesiatny")
    liczba_bin = input("Podaj liczbe w systmie binarnym: ")
    liczba_dz = 2 ** 5 * int(liczba_bin[-6]) + 2 ** 4 * int(liczba_bin[-5]) + 2 ** 3 * int(liczba_bin[-4]) + 2 ** 2 * int(liczba_bin[-3]) + 2 ** 1 * int(liczba_bin[-2]) + 2 ** 0 * int(liczba_bin[-1])
    print("Liczba w systemie dziesietnym to: ", liczba_dz)

elif wybrany_program == 7:
    print("Wybrano 7 Program do rozpoznawania czy podane liczba jest parzysta czy nie.")
    liczba = float(input("Podaj liczbe calkowita: "))
    if liczba % 2 == 0:
        print("Liczba jest parzysta.")
    elif liczba % 2 == 1:
        print("Liczba jest nieparzysta")
    else:
        print("Podana liczba nie jest cakowita.")

elif wybrany_program == 8:
    print("Wybrano 8 Program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7")
    liczba = int(input("Podaj liczbe calkowita= "))
    if liczba%3 == 0 or liczba%5 == 0 or liczba%7 == 0:
        print ("Liczba jest podzielna przez 3 lub 5 lub 7.")
    else:
        print("Liczba nie jest podzielnia przez zadna z liczb 3, 5, 7.")

elif wybrany_program == 9:
    print("Wybrano 9 Program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7")
    liczba = int(input("Podaj liczbe calkowita = "))
    if liczba%3 == 0 and liczba%5 == 0 and liczba%7 == 0:
        print ("Liczba jest podzielna przez 3 i 5 i 7.")
    else:
        print("Liczba nie jest podzielnia przez liczby 3, 5 i przez 7.")

elif wybrany_program == 10:
    print("Wybrano 10 Program do sprawdzania czy podany rok jest rokiem przestepnym")
    rok = int(input("Podaj rok = "))
    if rok%4 == 0:
        print ("Podany rok jest rokiem przestepnym.")
    else:
        print("Podany rok nie jest rokiem przestepnym.")