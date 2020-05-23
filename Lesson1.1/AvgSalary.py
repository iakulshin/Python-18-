count = 3 # Кол-во сотрудников
#git changing code reaction test
def AvgSalary(count):
    result = sum([int(input(f"Зарплата сотрудника #{i+1}: ")) for i in range(count)]) // count
    return f'Средняя зарплата сотрудников: {result} руб.'

print(AvgSalary(count))
