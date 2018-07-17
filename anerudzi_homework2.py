print("Uruchom odpowiedni program - wybierz od 1 do 10, zgodnie z ponizsza lista:")
print("1 Program TABELA")
print("2 Program wydawania monet")
print("3 Program rysowania piramidy")
print("4 Program do wyliczania wieku psa")
print("5 ")
print("6 Program KALKULATOR")
wybrany_program = int(input("   Wybieram program = "))

if wybrany_program == 1:
    print("Work in progress")
    input()

if wybrany_program == 2:
    print("Wybrano 2 Program wydawania monet")
    kwota = float(input("Wprowadz kwote: "))
    for i in [5, 2, 1, 0.5, 0.2, 0.1]:
        if int(kwota//i)!=0:
            print ("Wydaj ", int(kwota//i), "monet o wartosci ", i)
            kwota = kwota - (kwota//i)*i
        else:
            pass
    input()
    
if wybrany_program == 3:
    print("Wybrano 3 Program rysowania piramidy")
    wysokosc_piramidy = int(input("Jak wysoka ma byc piramida? "))
    b = wysokosc_piramidy * 2 - 1
    a = 1
    for x in range(wysokosc_piramidy):
        print(" " * b, "#" * a)
        b -=1
        a+=2
    input()
    
elif wybrany_program == 4:
    print("Wybrano 4 Program do wyliczania wieku psa")
    print("Przez pierwsze dwa lata, kazdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata")
    lata_ludzkie = int(input("Ile lat ludzkich zyje pies?"))
    if lata_ludzkie <= 2:
        wiek_psa = lata_ludzkie * 10.5
    else:
        wiek_psa = 2 * 10.5 + (lata_ludzkie - 2) * 4
    print ("Wiek psa = ", wiek_psa)
    input()
    
if wybrany_program == 5:
    print("Work in progress")

elif wybrany_program == 6:
    print("Work in progress")

else:
    pass
