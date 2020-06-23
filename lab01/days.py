import sys
from datetime import date
if len(sys.argv) < 2:
    print("Uruchamiajac skrypt podaj jako parametr datę!")
else:
    data = date.fromisoformat(sys.argv[1])
    today = date.today()
    
    datediff = today - data
    
    print("dzisiaj: "+str(today))
    print("odczytana data: "+str(data))
    print("różnica dni: "+str(datediff))