import math
import random
from datetime import datetime


#11 Напишите программу, вычисляющую значение тригонометрического выражения по заданному числу градусов x - sin x+cos x+tan2x
x = int(input('Введите угол: '))
radians_x = math.radians(x)

result = math.sin(radians_x) + math.cos(radians_x) + math.tan(2 * radians_x)
print(result)


#12 Выведите случайное целое число от 1 до 100.
random_int = random.randint(1, 100)
print(random_int)

#13 Выведите случайное вещественное число от 10,5 до 12,15.
random_float = random.uniform(10.5, 12.15)
print(random_float)

#14 Выберите случайным образом 1, 2, 3 элемента из списка случайных чисел, состоящего из 10 элементов.
random_numbers = [random.randint(1, 100) for _ in range(10)]
selected_elements = random.sample(random_numbers, random.randint(1, 3))
print(*selected_elements)

#15 Напишите программу, вычисляющую значение тригонометрического выражения при x = 1,42, y = 1,22 - 2∗cos(x−π6)1/2+sin2y+cos2x3∗ex
x = 1.42
y = 1.22

result = (2*math.cos(x - math.pi / 6))/(1/2 + math.sin(y)**2) + math.cos(x**3)**2 * math.exp(x)
print(result)

#16 Напишите программу, вычисляющую значение тригонометрического выражения при x = 3,033, y = 0,014.
x = 3.033
y = 0.014
result = (math.sin(x) + math.cos(y))/(math.cos(x) - math.sin(y)) * math.tan(x*y)
print(result)

# 17 Напишите программу, вычисляющую значение тригонометрического выражения при x = 3,033, y = 0,014.(Оно блять такое же как и 16, но я вставлю решение)
x = 3.033
y = 0.014
result = (math.sin(x) + math.cos(y))/(math.cos(x) - math.sin(y)) * math.tan(x*y)
print(result)

#18 Напишите программу, вычисляющую значение тригонометрического выражения при x = -1,255, y = 5,23.
x = -1.255
y = 5.23
result = math.log(abs(math.cos(x))) / math.log(1+x**2)
print(result)

#19 Сохраните в виде объекта datetime дату, представленную в форме строки "04/10/2023 11:30"
date_string = "04/10/2023 11:30"
date_object = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(date_object)

#20 Представьте в виде строки сегодняшнюю дату в формате YYYY-MM-DD HH:MM.
current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
print(current_date)

#21 Узнайте, какой день недели был 4 октября 2020 года.
weekDays = {
    "Sunday": "Воскресенье",
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота"
}
date_string = "04/10/2020"
date_object = datetime.strptime(date_string, "%d/%m/%Y")
day_of_week = date_object.strftime("%A")
print(weekDays[day_of_week])

#22 Напишите функцию date_range, которая возвращает количество дней между датами start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD
def date_range(start_date, end_date):
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date_obj - start_date_obj
    return delta.days

start_date = input('Начальная дата (YYYY-MM-DD): ')
end_date = input('Конечная дата (YYYY-MM-DD): ')
days_between = date_range(start_date, end_date)
print(f"Количество дней между датами: {days_between}")