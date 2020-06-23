import sys
import math
if len(sys.argv) < 4:
    print("Uruchamiajac skrypt podaj zmienne a,b,c")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    delta = b*b - (4*a*c)
    
    if delta < 0:
        print(0)
    if delta == 0:
        print(str((-b)/(2*a)))
    if delta > 0:
        print(str((-b-math.sqrt(delta))/(2*a))+" "+str((-b+math.sqrt(delta))/(2*a)))
    
