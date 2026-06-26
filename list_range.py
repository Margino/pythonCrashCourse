# Создать список квадратов всех целых чисел от 1 до 10
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# генератор списков
squares2 = [value ** 2 for value in range(1,11)]
print()
print(squares2)

# min, max, sum
digits = list(range(1,100,5))

print()
print(digits)
print("min:", min(digits))
print("max:", max(digits))
print("sum:", sum(digits))


names = []
names_upper = []
#names_upper = [name.upper() for name in names]
for name in names:
    names_upper.append(name.upper())

numbers = []
evens = []
#evens = [x for x in numbers if x % 2 == 0]
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

file = []
lines = []
#lines = [line.strip() for line in file]
for line in file:
    lines.append(line.strip())


# 1-20
print()
for num in range (1,21):
    print(num)

# list 1-1_000_000
lemon = list(range(1,1_000_001))
for num in lemon:
    #print(num)
    pass

print()
print("max:", max(lemon))
print("sum:", sum(lemon))

# 1-20, odd

odd_list = list(range(1,21,2))
print()
print(odd_list)

# 1-30 % 3 == 0

# multiplyThree = []
# for num in range (3, 31):
#     if num % 3 == 0:
#         multiplyThree.append(num)

# multiplyThree = [num for num in range(3, 31) if num % 3 == 0]

multiplyThree = list(range(3, 31, 3))

print()
print(multiplyThree)

# 1 - 10 ** 3

cube = []
for num in range(1, 11):
    cube.append(num ** 3)

print()
print(cube)

cube2 = [num ** 3 for num in range(1, 11)]

print()
print(cube2)