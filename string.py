# имя пользователя
user_name = "John Doe"
user_name_low = user_name.lower()

print(f"Hello {user_name}! Don't you want to learn Python today?")

print(user_name.lower())
print(user_name.upper())
print(user_name_low.title())

# знаменитая цитата
person_name = "Астап Бендер"
famous_quote = "А может быть тебе дать ключ от квартиры где деньги лежат?"
message = f"{famous_quote} ({person_name})"
print(message)

# удаление пробелов
user_name_spaces = "   John Doe  "
print(user_name_spaces, ".", sep="")
print(user_name_spaces.lstrip(), ".", sep="")
print(user_name_spaces.rstrip(), ".", sep="")
print(user_name_spaces.strip(), ".", sep="")

# расширение файлов
file_name = "python_notes.txt"
print(file_name.removesuffix('.txt'))

