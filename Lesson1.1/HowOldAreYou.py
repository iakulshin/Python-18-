from datetime import *

birthday = date.fromisoformat(input('Введите дату формата ГГГГ-ММ-ДД: '))

def HowOldAreYou(birthday):
    today = date.today()
    return f'Ваш возраст: {int((today - birthday).days / 365.25)}'

print(HowOldAreYou(birthday))
