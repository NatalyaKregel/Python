# ЗАДАЧА №1: Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

import math 
n = int(input('Введите число: '))
pi = math.pi
print('Полное число ПИ:', +pi)
print('Число ПИ с точнойстью до', n , 'знаков после запятой: ', (round(pi, n)))


