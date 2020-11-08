class Card(object):
    # Cоздание одной игральной карты. Если присвоить значение переменной с атрибутами rank и suit.
    # пример one_card = Card(rank='4', suit='s').
    """ Одна  игральная  карта."""
    RANKS = ["А",  "2",  "З",  "4",  "5",  "6",  "7",  "В",  "9",  "10",  "J",  "Q",  "К"]
    SUITS = ["с",  "d",  "h",  "s"]
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
    def __str__(self): # Соединяет в одну строку rank и suit и возвращает для вывода на печать.
        if self.is_face_up: # если карта открыта (face_up = True)
            rep = self.rank + self.suit # выводится масть и ранг карты
        else:
            rep = 'XX' # Если карта закрыта (face_up = False) выводится "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    # Cоздание пустого списка карт, в который в последствии будут добавляться карты по одной.
    """ Рука :  набор  карт  на  руках у  одного  игрока."""
    def __init__(self): # возвращает одной строкой всю руку. Метод последовательно берет все 
        # объекты класса Card и соединяет их строковые представления. Если в составе объекта 
        # Hand нет ни однойкарты, то будет возвращена строка <пусто>.
        self.cards = []
    def __str__(self): 
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '<пусто>'
        return rep
    def clear(self): # очищает список карт
        self.cards = []
    def add(self, card): # добавляет объект к списку cards
        self.cards.append(card)
    def give(self, card, other_hand): # удаляет объект из списка cards, принадлежащий данной руке, 
        # и добавляет тот же объект в набор другого класса Hand. 
        # Пример:
        # my_hand = Hand() 
        # your_hand= Hand()
        # my_hand.give(card1, your_hand)
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand): # наследует все методы класса Hand. В данном случае Hand является базовым классом, а Deck производным.
    """Колода игральных карт"""
    # дополнительные методы. Расширение производного класса.
    def populate(self): # создаем колоду из 52 карт
        self.cards = [] # создается пустой список cards
        for suit in Card.SUITS: # извлекает масти карт из списка
            for rank in Card.RANKS: # извелкаем ранги карт из списка
                self.add(Card(rank, suit)) # добавляем все карты в список cards
    def shuffle(self):  # перемешиваем колоду карт
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand=1): #раздает в каждую руку по одной(по умолчанию) карте. 
        #Принимает два аргумента список рук и количество карт.
        # Пример:
        # my_hand = Hand()
        # your_hand = Hand()
        # hands = [my_hand, your_hand]
        # coloda.deal(hands, per_hand=5) - раздается по 5 карт в две руки (если дадим на печать coloda то увидим что в ней осталось 42 карты)
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('He  могу  больше  сдавать:  карты  закончились!')

if __name__ == '__main__':
    print('Этo  модуль.содержащий  классы  для  карточных  игр.')
