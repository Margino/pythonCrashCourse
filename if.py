#'green', 'yellow', 'red'

alien_color = 'green'
#alien_color = 'yellow'

if alien_color == 'green':
    print('Вы заработали 5 очков')

print()
if alien_color == 'yellow':
    print('Вы заработали 5 очков')
else:
    print('Вы заработали 10 очков')

print()
if alien_color == 'green':
    print('Вы заработали 5 очков')
elif alien_color == 'yellow':
    print('Вы заработали 10 очков')
else:
    print('Вы заработали 15 очков')

age = 64

print()
if age < 2:
    print('младенец')
elif age < 4:
    print('малыш')
elif age < 13:
    print('ребенок')
elif age < 20:
    print('подросток')
elif age < 65:
    print('взрослый')
else:
    print('пожилой человек')


favorite_fruits = ['апельсин','арбуз','банан']

print()
if 'апельсин' in favorite_fruits:
    print(f'Вы очень любите апельсины!')
if 'арбуз' in favorite_fruits:
    print(f'Вы очень любите арбузы!')
if 'банан' in favorite_fruits:
    print(f'Вы очень любите бананы!')

users = ['admin', 'ivan', 'sergey', 'dmitriy', 'gosha']
# users = []

print()
if users:
    for user in users:
        if user == 'admin':
            print('Здравствуйте, admin, хотите просмотреть отчет о состоянии дел?')
        else:
            print(f'Привет, {user.title()}, спасибо, что авторизовался в системе')
else:
    print('Нам нужно добавить несколько пользователей!')


current_users = ['admin', 'Ivan', 'sergey', 'dmitriy', 'gosha']
new_users = ['ivan', 'inna', 'dmitriy', 'roma', 'olga']

print()
if current_users and new_users:
    # current_users_upp = []
    # for user in current_users:
    #     current_users_upp.append(user.lower())
    current_users_upp = [user.lower() for user in current_users]

    for user in new_users:
        if user.lower() in current_users_upp:
            print(f'* Имя {user} уже занято. Пожалуйста, выберите другое имя. *')
        else:
            print(f'Имя {user} доступно для регистрации.')

# th кроме 1st, 2nd и 3rd
numbers = list(range(1,10))

print()
if numbers:
    for num in numbers:
        if num == 1:
            print(f'{num}st')
        elif num == 2:
            print(f'{num}nd')
        elif num == 3:
            print(f'{num}rd')
        elif 4 <= num <= 9:
            print(f'{num}th')
        else:
            print('Число вне диапазона задачи!')