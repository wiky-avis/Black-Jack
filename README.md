# Black-Jack

Классы игры Блек-Джек

ВJ_carc1 - carcls.card - Карта для игры в «Блек-джек». Дополнительно к атрибутам базового класса объявляет атрибут value -количество очков, соответствующее данной карте.

ВJ_Deck - cards.Deck - Колода для игры в «Блек-джек». Представляет собой набор объектов BJ_Card.

ВJ_Hand - cards.Hand - «Рука» игрока в «Блек-джек». Объявляет атрибугы: name, представ-ляющий имя игрока, и total, равный сумме очков на руках у этого игрока.

ВJ_Player - ВJ_Hand - Игрок в «Блек-джек».

ВJ_Dealer - ВJ_Hand - дилер (сдающий при игре в «Блек-джек»).

ВJ_Game - object - Игра в «Блек-джек». Объявляет атрибугы: deck со значением -объ-ектом ВJ_Deck, dealer со значением -объектом ВJ_Dealer и players, ссылающийся 
                   на список объектов ВJ_Player.
