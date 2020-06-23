import sys
if len(sys.argv) < 2:
    print("Uruchamiajac skrypt podaj co najmniej jeden parametr!")
else:
    ilosc = 0
    wyrazy = []
    for x in range(1,len(sys.argv)):
        if(len(sys.argv[x])>=3):
            ilosc+=1
            wyrazy.insert(0,sys.argv[x])
    
    print("ilosc argumentów dłuższych lub równych 3 znaki = "+str(ilosc))
    print("argument dłuższe lub równe 3 od końca = "+" ".join(wyrazy))