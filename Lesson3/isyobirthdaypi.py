file = open('pi_million_digits.txt', 'r', encoding='utf-8')
pi = ''.join(file.readlines())

your_birthday = input('Введит свой день рождения вида ДДММГГ,\n'
                      'Пример: 020595: ')

print(your_birthday in pi)
