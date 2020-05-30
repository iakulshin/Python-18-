import os, random, string

file_name_data = 'data.txt'
file_name_discount = 'discount.txt'

# Читаем файлы
file_data = open(file_name_data, 'r', encoding='utf-8')
file_discount = open(file_name_discount, 'r', encoding='utf-8')

# Формируем словарь вида {Клиент: Деньги}
dict_data = dict([i.split(',') for i in file_data.read().splitlines()])
list_discount = [dis for dis in file_discount.read().splitlines()]

result = list()

# Закрываем файлы
file_data.close()
file_discount.close()

def apply_discount(dict_data, list_discount):

    """ Принимаем на вход данные о товаре в виде словаря и скидку"""
    for data, dis in zip(dict_data.items(), list_discount):
        price = int(data[1]) * float(dis)
        result.append((data[0], price))

        try:
            assert 0 <= price <= int(data[1])
        except AssertionError:
            print(f"Проверьте файл {file_name_discount}, отрицательная цена товара!")
            exit(0)
    return result

def generate_random_name(length=10):

    """ Генерируем рандомное имя и проверяем нет ли его в списке файлов корневой папки """
    name = ''.join([random.choice(string.ascii_lowercase) for _ in range(length)]) + '.txt'

    while name in os.listdir('.'):
        name = ''.join([random.choice(string.ascii_lowercase) for _ in range(length)]) + '.txt'

    return name

result = apply_discount(dict_data, list_discount)

with open(generate_random_name(), 'w', encoding='utf-8') as out_file:
    for sku in result:
        out_file.write(f'{sku[0]}, {sku[1]}' + '\n')
