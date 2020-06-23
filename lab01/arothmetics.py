import sys
if len(sys.argv) < 4:
    print("Uruchamiajac skrypt podaj jako parametr zmienna a, działanie, zmienna b!")
else:
    a = sys.argv[1]
    znak = sys.argv[2]
    b = sys.argv[3]
    wynik = a
    
    if znak == "+":
        wynik = int(a)+int(b)
    if znak == "-":
        wynik = int(a)-int(b)
    if znak == "*":
        wynik = int(a)*int(b)
    if znak == "/":
        wynik = int(a)/int(b)

    print(a+znak+b+"= "+str(wynik))