file_name = 'data.txt'
file = open(file_name, 'r', encoding='utf-8')

# Формируем словарь вида {Клиент: Деньги}
data_dict = dict([i.split() for i in file.read().splitlines()])

# Приводим значения к типу int
sum = sum([int(a) for a in data_dict.values()])

# Находим среднее
avg = sum // len(data_dict.values())

with open('output.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(f'Общий баланс: {sum}' + '\n')
    out_file.write(f'Средний баланс: {avg}')
