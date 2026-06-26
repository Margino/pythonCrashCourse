cars_list = ['BMW', 'Opel', 'Mersedes', 'Lada', 'Pegeout', 'Renault', 'Honda']
middle_element = len(cars_list) // 2

print(f"These are the three first elements of the list: {cars_list[:3]}")
print(f"These are the three middle elements of the list: {cars_list[middle_element-1:middle_element+2]}")
print(f"These are the three last elements of the list: {cars_list[-3:]}")


my_pizzas = ['с колбасой', 'с ананасами', 'с грибами', 'c луком']
friend_pizzas = my_pizzas[:]
print()
print(f"Мои пиццы: {my_pizzas}")
print(f"Пиццы моего друга: {friend_pizzas}")

my_pizzas.append('с курицей')
friend_pizzas.append('с бананами')

print()
print(f"Мои любимые пиццы:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print()
print(f"Любимые пиццы моего друга:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

