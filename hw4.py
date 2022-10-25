# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код,
#  загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

print(f'ФИО пользователей:')
users = ['Ivanov Ivan Ivanovich', 'Petrov Petr Petrovich']
with open('users.txt', 'w') as f:   
    f.write(str(users[0]))
    f.write('\n')
    f.writelines(str(users[-1]))
with open('users.txt') as file:
    my_str = file.read()
my_list = [str(x) for x in my_str.split('\n')]
print(my_list)

print('Хобби пользователей:')
hobby = 'rock climbing, hunting', 'downhill skiing'
with open('hobby.txt', 'w') as f1:
    f1.write(str(hobby[0]))
    f1.write('\n')
    f1.writelines(str(hobby[-1]))
with open('hobby.txt') as file1:
    my_str1 = file1.read()
my_list1 = [str(x1) for x1 in my_str1.split('\n')]
print(my_list1) 
print()

keys = my_list
values = my_list1
info = dict(zip(keys, values))
print('Словарь:')
print(info)

users_hobby = str(info)
with open('users_hobby.txt', 'w') as uh:   
    uh.write(users_hobby)


# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
new_list = []
for i in range(1, number+1):
    if(number % i == 0):
      new_list.append(i)
print(f'Для числа {number} список простых множителей = {new_list}')


# 32. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

number = [8, 2, 5, 4, 5, 6, 3, 8, 3]
number1 = set(number)
print(number1)



# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint
a = randint (1, 100)
b = randint (1, 100)
c = randint (1, 100)
print(f'a = {a}, b = {b}, c = {c}')
k = int(input('Введите натуральную степень: '))
str1 = str(f'{a}x**{k} + {b}x + {c} = 0 ')
print(str1)
file = str1
with open('str1.txt', 'w') as f:   
    f.writelines(str(str1))