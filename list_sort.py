country_list = ['Germany', 'Canada', 'France', 'Finland', 'Italy']

print("I'd like to visit:", country_list)

print()
print("Sorted list:", sorted(country_list))

print()
print("Initial list:", country_list)

print()
print("Reverse sorted list:", sorted(country_list, reverse=True))

print()
print("Initial list:", country_list)

country_list.reverse()
print()
print("Reversed list:", country_list)

country_list.reverse()
print()
print("ReReversed list:", country_list)

country_list.sort()
print()
print("Sorted list", country_list)

country_list.sort(reverse=True)
print()
print("Reversed sorted list:", country_list)


cars_list = ['BMW', 'Opel', 'Mersedes', 'Lada', 'Pegeout', 'Renault', 'Honda']

print()
print(cars_list)

cars_list.sort()
print()
print(cars_list)

print()
print(sorted(cars_list, reverse=True))

cars_list.reverse()
print()
print(cars_list)

print()
print(len(cars_list))