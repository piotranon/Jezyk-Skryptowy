import random

class Card:
    # słownik symboli unicode
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
       
    def __init__(self, rank, suit):
    # TODO: definicja metody
        self.rank =rank
        self.suit =suit

    def get_value(self):
    # TODO: definicja metody (ma zwracać kartę w takiej reprezentacji, jak dotychczas, tzn. krotka)
        return self

    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty
        card=""+self.rank+str(Card.unicode_dict.get(self.suit))
        return card
class Deck():
    def __init__(self, *args):
    # TODO: definicja metody, ma tworzyć niepotasowaną talię (jak na poprzednich lab)
        self.deck =[]
        for suit in ['s', 'd', 'h', 'c']:
                for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']:
                    self.deck.append(Card(rank,suit))      
    
    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty
        deckStr="["
        for c in self.deck:
            deckStr+=str(c)+","
        deckStr = deckStr[:-1]
        deckStr+="]"
        return deckStr

    def shuffle(self):
    # TODO: definicja metody, tasowanie
        random.shuffle(self.deck)
        return 1
    def deal(self, players):
    # TODO: definicja metody, otrzymuje listę graczy i rozdaje im karty wywołując na nich metodę take_card z Player
        for i in range(5):
            for player in players:
                player.take_card(self.deck.pop())
        return players
    def show(self):
        cards="["
        for card in self.deck:
            cards+=str(card)+","
        cards=cards[:-1]
        cards+="]"
        print(cards)
class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
    # TODO: definicja metody, zwraca stringa z kartami gracza
        cards=""
        for card in self.__hand_:
            cards+=card.rank+str(Card.unicode_dict.get(card.suit))+","
        cards = cards[:-1]
        return cards

def histogram(text):
# TODO: wstawić metodę z poprzedniego lab
    dictionary = {}
    
    for character in text:
        if character != " ":
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
            
    return dictionary
    pass

# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}

def is_rank_sequence(hand):
    
    #order = ['2','3','4','5','6','7','8','9','10','J','D','K','A']
    order = ['A','K','D','J','10','9','8','7','6','5','4','3','2']
    
    cardIterator = order.index(hand[0].rank)#getting index of card in order[] of first card in hand
    
    inOrder=1#we take that order is correct at start
    #if there isn't 4 more cards after iterator its it not possible
    if cardIterator>len(order)-len(hand):
        cardIterator=0
        inOrder=0
        return inOrder
        
    for card in hand:#iterating thru whole cards
        #checking if card rank matches order[]
        if card.rank!=order[cardIterator]:
            inOrder=0
            
        cardIterator+=1
    
    return inOrder
def get_player_hand_rank(hand):
# TODO: wstawić metodę z poprzedniego lab
    hand_rank_list = []  # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_color_list = [] # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.

#    print("Cards:")
    for card in hand:
        hand_rank_list.append(card.suit)
        hand_color_list.append(card.rank)

    
#    print("---------DATA-----------")
    
    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    # TODO: uzyj funkcji 'histogram' z poprzedniego laboratorium!
    
    hand_rank_histogram = histogram(hand_rank_list)
#    print("histogram rank: "+str(hand_rank_histogram.items()))
#    print("histogram rank list: "+str(list(hand_rank_histogram.values())))
    
    # histogramy kolorow kart graczy, jesli 5 in hand_color_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    
    hand_color_histogram = histogram(hand_color_list)
#    print("histogram colors: "+str(hand_color_histogram.items()))
#   print("histogram colors list: "+str(list(hand_color_histogram.items())))
    
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    # TODO: zaimplementuj funkcje is_rank_sequence(hand) ktora zwraca True jesli karty sa po kolei
    #       w przeciwnym razie zwraca false. Pobiera liste kart jako parametr
    
    is_hand_rank_sequence = is_rank_sequence(hand)
#    print("is in order: "+str(is_hand_rank_sequence))

    hand_strength = 0 # zwracana zmienna, ja trzeba ustawic
    # ------ sprawdzamy uklad gracza 1:
    
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    #poker krolewski (Royal flush)
    if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
        
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    #poker (Straight flush)
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
        
    # --- sprawdzamy kareta: 4 karty z tą samą wartościa
    #Kareta (Four of a kind)
    elif(4 == list(hand_rank_histogram.values())[0]):
        hand_strength =  8
        
    # --- sprawdzamy ful: 3 karty z tą samą wartościa, 2 karty z tą samą wartościa
    #ful (Full house)
    elif(3 == list(hand_rank_histogram.values())[0] and 2 == list(hand_rank_histogram.values())[1] or 3 == list(hand_rank_histogram.values())[1] and 2 == list(hand_rank_histogram.values())[0]):
        hand_strength =  7
        
    # --- sprawdzamy kolor: 5 kart z tym samym kolorem
    #kolor (flush)
    elif(5 in hand_color_histogram.values()):
        hand_strength =  6
        
    # --- sprawdzamy strit: 5 kart po sobie, conajmniej jedna w innym kolorze, dozwolone ('5','4','3','2','A')
    #strit (Straight)
    elif((is_hand_rank_sequence or hand[0].rank=='5' and hand[1].rank=='4' and hand[2].rank=='3' and hand[3].rank=='2' and hand[4].rank=='A') and 5 not in hand_color_histogram.values()):
        hand_strength = 5
    
    # --- sprawdzamy trojka: 3 karty z tą samą wartościa
    #trojka (Three of a kind)
    elif(3 in list(hand_rank_histogram.values())):
        hand_strength = 4
    
    # --- sprawdzamy dwie pary:2 x 2 karty z tą samą wartościa
    #dwie pary (Two pair)
    elif(2 == list(hand_rank_histogram.values())[0] and 2 == list(hand_rank_histogram.values())[1] or 2 == list(hand_rank_histogram.values())[1] and 2 == list(hand_rank_histogram.values())[2] or 2 == list(hand_rank_histogram.values())[0] and 2 == list(hand_rank_histogram.values())[2]):
        hand_strength = 3
    
    # --- sprawdzamy jedna pare: 2 karty z tą samą wartościa
    #jedna pare (One pair)
    
    
    elif(2 in hand_rank_histogram.values()):
        hand_strength = 2    
    
    # --- sprawdzamy wysoka karta: 2 karty z tą samą wartościa, 2 karty z tą samą wartościa
    #wysoka karta (High card)
    else:
        hand_strength = 1
        
    return(hand_strength)
 
#talia = Deck()

#print("Nowa talia:")
#talia.show()
#print("========================")

#talia.shuffle()

#print("Talia potasowana:")
#talia.show()
#print("========================")

#number_of_players = 2
#players = [Player(1000) for i in range(number_of_players)]

#talia.deal(players)
#i=1
#for player in players:
#    print("Karty gracza "+str(i))
#    i+=1
#    print(player.cards_to_str())
#    print("-----------------------------")

#print("Talia po rozdaniu:")
#talia.show()
#print("========================")