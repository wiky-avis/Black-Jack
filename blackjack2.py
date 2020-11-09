# coding= utf-8

# Добавьте в игру «Бnек-джек» проверку на ошибки. Перед началом очередного раунда 
# надо проверять достаточно ли карт в колоде. Есnи нет, колоду сnедует вновь наполнить 
# и перемешать. Найдите в программе и другие уязвимые места, которым не помешает 
# проверка на ошибки или перехват искnючений.

# Доработайте проект «Блек-джек» так, чтобы игроки могли делать ставки. Программа 
# должна следить за капи­талом каждого игрока и выводить из-за стола тех, у кого закончатся деньги.


import cards, games

class BJ_Card(cards.Card): # расширяет функциональность своего базового класса саrds.Саrd
    """Карта  для  игры  в  Блек-джек."""
    ACE_VALUE = 1
    @property
    def value(self): # создается новое свойство value, представляющее номинал карты, возвращает число из диапазона от 1 до 1О
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1 #Эта конструкция берет атрибут rank объекта-карты, то есть ее истин­ный номинал (например, "6" ), и находит порядковый номер этого номинала в списке BJ_Саrd.RANKS (для шестерки это 5 ). Затем к полученному значению прибавляется единица, потому что компьютер начинает считать с О (таким образом, от строкового "6" мы перейдем к целочисленному 6). 
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    """Колода  для  игры  в  "Блек-джек". """
    def populate(self): # переопределен метод cards.Deck's  populate(), и теперь новая колода класса BJ_Deck 
        # наполняется картами класса BJ_Card
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
    
    def __len__(self):
        return len(self.cards)
    
    def number_is_cards(self): # вычисляем количество карт в нашей стандартной колоде
        print('RANKS', BJ_Card.RANKS)
        print('SUITS', BJ_Card.SUITS)
        m = str(len(BJ_Card.RANKS) * len(BJ_Card.SUITS))
        return m


class BJ_Hand(cards.Hand):
    """Рука:  набор  карт  "Блек-джека"  у  одного  игрока."""
    def __init__(self, name): # переопределен конструктор cards.Hand, добавив в него атрибут name, представляющий имя обладателя данной руки
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self): # переопределен так что он теперь отображает сумму очков на руках у игрока
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep
    @property
    def total(self):
        # если у одной из кард value равно None, то и все свойство равно None
        for card in self.cards:
            if not card.value:
                return None
        # суммируем очки, считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value
        # определяем есть ли туз у игрока на руках
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        # если на руках есть туз и сумма очков не превышает 11, 
        # будем считать туз за 11 очков
        if contains_ace and t <= 11:
            # прибавить  нужно  лишь  10.  потому  что  единица  уже  
            # вошла  в  общую сумму
            t += 10
        return t
    def is_busted(self): # возвращает True, когда свойство total объекта принимает значение больше 21. В противном случае будет возвращено False.
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Игрок в Блек-Джек"""
    def is_hitting(self): # возвращает True в том случае, если игроку угод­но получить еще карту, и False - если нет
        response = games.ask_yes_no('\n' + self.name + ', будете брать еще карты? (Y/N): ')
        return response == 'y'
    def is_rate(self): # Ставка игрока
        rate = games.ask_number(self.name + ', мы принимаем ставки от 10 до 500 руб, сколько хотите поставить? : ', low = 10, hight = 500)
        return rate
    def bust(self): # объявляет, что участник перебрал
        print(self.name, 'перебрал.')
        self.lose()
    def lose(self): # объявляет, что участник проиграл
        print(self.name, 'проиграл.')
    def win(self): # объявляет, что участник выиграл
        print(self.name, 'выиграл.')
    def push(self): # объявляет ничью
        print(self.name, 'сыграл с компьютером в ничью.')


class BJ_Dealer(BJ_Hand):
    """Дилер в игре Блек-Джек"""
    def is_hitting(self): # определяет, будет ли дилер брать дополнитель­ные карты
        return self.total < 17 #  имея на руках не более 17 очков, обязан тянуть оче­редную карту, метод возвращает True,  если свойство tota l объекта не превыша­ет 17, а в противном случае возвращает False
    def bust(self): # объявляет, что дилер перебрал
        print(self.name, 'перебрал')
    def flip_first_card(self): #  переворачивает первую карту дилера лицевой стороной вниз
        first_card = self.cards[0]
        first_card.flip()
        

class BJ_Game(object): #  используется для создания объектов, которые будут представлять отдельные игры
    """Игра в Блек-Джек"""
    def __init__(self, names): # Конструктор принимает список имен и создает на каждое имя по игроку. Кроме того, будут созданы дилер и колода
        self.players = []
        self.pl_rt = {}
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
            rate1 = player.is_rate()
            self.pl_rt[name] = rate1
            print(self.pl_rt)
        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.lend = str(len(self.deck)) # узнаем сколько карт в созданной колоде
        self.lend2 = BJ_Deck().number_is_cards() # передаем сколько карт должно быть в колоде
        if self.lend == self.lend2: # проверяем достаточно ли карт в колоде
            print('В колоде достаточно карт\n')
        else:
            print('В колоде недостаточно или перебор карт. Создаю новую колоду и перемешиваю.\n')
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
        
    @property
    def still_playing(self): # возвращает список игроков еще не перебравших в текущем раунде
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player): # сдает игроку или дилеру дополнительные карты. Этот метод принимает в свой параметр 
        # player объект класса BJ_Player или BJ_Dealer. До тех пор пока метод is_busted() данного объекта возвращает False,
        # а метод is_hitting() возвращает True, программа будет сдавать карты.
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # сдача всем по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card() #первая из карт, сданных диллеру, переворачивается рубашкой вверх
        for player in self.players:
            print(player) #  на экран выводятся <руки> всех участников игры
        print(self.dealer)
        # сдача дополнительных карт игрокам
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card() #это первая карта дилера раскрывается
        if not self.still_playing:
            # все игроки перебрали, покажем только "руку" дилера
            print(self.dealer)
        else:
            # сдача дополнительных карт
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                # выигрывают все, кто еще остался в игре
                for player in self.still_playing:
                    player.win()
            else:
                # сравниваем суммы очков у диллера и у игроков, оставшихся в игре
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main(): # принимает имена всех игроков, организует их в виде списка и соз­дает объект BJ_ Game, 
    # которому этот список передается как аргумент.
    print('\t\tДoбpo  пожаловать  за  игровой  стол  Блек-джека!\n')
    names = []
    number = games.ask_number('Cкoлькo  всего  игроков?  (1  - 7):  ', low = 1, hight = 8)
    for i in range(number):
        name = input('Введите  имя  игрока:  ')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n': # Затем функция вызывает метод рlау() данного объекта и будет делать это снова и 
        # снова до тех пор, пока игроки не изъявят желание прекратить игру.
        game.play()
        again = games.ask_yes_no('\nXoтитe сыграть  еще  раз?  ')


main()
input('\n\nНажмите  Enter.  чтобы  выйти.')
