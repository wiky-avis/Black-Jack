# Игры
# Демонстирует создание модуля
class Player(object):
    """Участник игры"""
    def __init__(self, name, score = 0): #создается игрок с двумя свойствами name и score
        self.name = name 
        self.score = score
    def __str__(self):
        rep = self.name + ':\t' + str(self.score) # возвращает строку с теми же двумя свойствами
        return rep

def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'. """
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower() # принимает текст вопроса и возвращает букву y или n
    return response

def ask_number(question, low, hight):
    """Просит ввести число из заданного диапазона. """
    response = None
    while response not in range(low, hight): # принимает текст вопроса, нижнюю и верхнюю границу 
        # диапазона, а возвращает число из этого диапазона
        response = int(input(question))
    return response

if __name__ == '__main__': # истинно только тогда когда программа запущенна напрямую.
    # если она импортируется в качестве модуля,то условие ложно.
    print('Bы  запустили  этот  модуль  напрямую.  а  не  импортировали  его.')
