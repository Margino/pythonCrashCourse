buffet = ('картошка','салат','суп','шашлык','кофе')

def print_menu (buffet):
    """"Выводит элементы кортежа построчно"""
    for dish in buffet:
        print(f'- {dish}')

print('Наш ресторан предлагает следующие блюда:')
print_menu(buffet)

# проверяем наличие ошибки
# buffet[0] = 'капуста'

# вариант со срезом
#buffet = buffet[2:] + ('лук','капуста')

# самый читаемый вариант
buffet = list(buffet)
buffet[1] = 'лук'
buffet[3] = 'капуста'
buffet = tuple(buffet)

print()
print('Наше новое меню:')
print_menu(buffet)