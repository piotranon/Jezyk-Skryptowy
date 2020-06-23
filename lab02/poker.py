import random

class Karta:
    def __init__(self, ranga, kolor):
        self.ranga =ranga
        self.kolor =kolor
        
    def show(self):
        print("('"+self.ranga+"', '"+self.kolor+"')")
        
class Gracz:
    def __init__(self):
        self.karty = []
    
    def  __str__(self):
        karty = "["
        for k in self.karty:
            karty+="('"+k.ranga+"', '"+k.kolor+"'),"
        karty = karty[:-1]
        karty+="]"
        return karty
        
    def show(self):
        for k in self.karty:
            k.show()
            
def Deck():
    talia =[]
    for kolor in ['Pik', 'Karo', 'Kier', 'Trefl']:
            for ranga in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']:
                talia.append(Karta(ranga,kolor))      
    return talia;

def show(deck):
    print("Talia :")
    for k in deck:
        k.show()

def shuffle_deck(deck):
    random.shuffle(deck)

def deal(deck,n):
    gracze = [Gracz() for i in range(n)]
        
    for i in range(5):
        for gracz in gracze:
            gracz.karty.append(deck.pop())
            
    return gracze

talia = Deck()

shuffle_deck(talia)
show(talia)
gracze = deal(talia,2)

print()
for gracz in gracze:
    print(str(gracz))