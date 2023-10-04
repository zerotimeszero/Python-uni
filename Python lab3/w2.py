'''
from statistics import mean
def sum_transitions(company, stat):
    new = list(map(lambda x: int(x.split(',')[2]),list(filter(lambda x: company in x,stat))))
    return [min(new),max(new),mean(new)]
ad_stats = [
    '2023-01-01,vk,43',
    '2023-01-01,fb,775',
    '2023-01-01,ya,64',
    '2023-01-02,vk,1164',
    '2023-01-02,fb,35',
    '2023-01-02,ya,254',
    '2023-01-02,ok,645',
    '2023-01-03,vk,7754',
    '2023-01-03,fb,654',
    '2023-01-03,ya,4625',
    '2023-01-03,ok,245',
]
company = input('Введите название кампании: ')
result = sum_transitions(company,ad_stats)
print(f"Минимальное - {result[0]}\nМаксимальное - {result[1]}\nСреднее - {result[-1]}")
'''
#2

from Currency import Rate
'''
print("Пункты 1|2")
print('------------------------------------------------\n')
curr = Rate('full')
print(curr.usd())
print('\n------------------------------------------------')
print('Пункт 3')
print(Rate('wName').make_format('USD'))
print('\n------------------------------------------------')
print('Пункт 4')
print(curr.usd(True))
print('\n------------------------------------------------')
print('Пункт 5')
print(curr.get_currency_info('EUR'))
print('\n------------------------------------------------')
print('Пункт 6')
print(curr.max_currency())
print(curr.min_currency())
print('\n------------------------------------------------')
print('Пункт 7')
print(curr.usd_for_weeks(5))
print('\n------------------------------------------------')
print('Пункт 8')
print(curr.currency_for_weeks('EUR'),5)
'''

from Matrix import Matrix

matrix = Matrix(2,2)
matrix.input_matrix()
print('\nМатрица:\n')
matrix.print_matrix()
print('\n------------------------------------------------')
print('Сумма i-ого столбца')
print(matrix.column_sum(1))
print('\n------------------------------------------------')
print('Кол-во нулей')
print(matrix.zero_count())
matrix.set_diagonal(5)
print('\n------------------------------------------------')
print('Матрица после замены элементов главной диагонали')
matrix.print_matrix()
