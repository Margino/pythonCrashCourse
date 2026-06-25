def sent_invites(guests):
    if not guests:
        print("Список гостей пустой!")
        return

    for guest in guests:
        print(f"Дорогой {guest}, приглашем тебя на вечеринку!")


def change_guest(guests, old_guest, new_guest):
    if old_guest not in guests:
        print()
        print("Замена не произведена. Нет гостя которого надо удалить!")
        return guests
    
    for i in range(len(guests)):
        if guests[i] == old_guest:
            guests[i] = new_guest
            break

    print()
    print(f"Так как {old_guest} не смог придти, к нам придёт {new_guest}")

    return guests


guests_list = ['Иван', 'Олег', 'Глеб', 'Яков', 'Мирон', 'Миша', 'Глеб']

print()
print("Cписок приглашений:")
sent_invites(guests_list)

change_guest(guests_list, 'Глеб', '*Матвей*')

print()
print("Новый список приглашений:")
sent_invites(guests_list)

print()
print("Ура мы нашли стол большего размера! Теперь мы ждём больше гостей!!!")

guests_list.insert(0,'-Слава-')
guests_list.insert(len(guests_list)//2,'-Ярик-')
guests_list.append('-Жора-')

print()
print("Новый список приглашений:")
sent_invites(guests_list)


guests_remained = 2
print()
print(f"К сожалению привести новый стол не успевают. Не вечеринку приглашены только {guests_remained} гостя :(\n")

for i in range(len(guests_list) - guests_remained):
    print(f"Дорогой {guests_list.pop()}, к сожалнию, ваше приглашение на вечеринку отменено.")


print()
for guest in guests_list:
    print(f"Дорогой {guest}, ваше приглашение на вечеринку остаётся в силе!")

while guests_list:
    del guests_list[0]

print()
print("Гости закончились!", guests_list)