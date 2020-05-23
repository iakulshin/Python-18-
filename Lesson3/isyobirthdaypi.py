from math import pi
from decimal import Decimal

your_birthday = input('Введит свой день рождения вида ДДММГГ,\n'
                      'Пример: 020595: ')

top_accuracy = Decimal(pi)
print(your_birthday in str(top_accuracy))

