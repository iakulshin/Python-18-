import random

amount_of_words = input("Как много слов вы хотите занести в словарь")
aow = int(amount_of_words)
slovar = {}

for i in range(aow):
    key = input("Введите слово на английском \n:")
    value = input("Введите слово на русском \n:")
    slovar[key] = value

# перемешиваем список
result = list(slovar.keys())
random.shuffle(result)

for key in result:
    print("Переведи слово", key, ": ")
    answer = input("Ваш вариант перевода\n:")
    if slovar[key] == answer:
        print("Все верно! Лев сыт!")
    else:
        print("А правильный овет был", slovar[key])