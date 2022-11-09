# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

A=[]    # массив для сохранения координат точки А 
for i in range(2):
    number = float(input('Введите координаты точки A: '))
    A.append(number)
B=[]    # массив для сохранения координат точки B 
for i in range(2):
    number = float(input('Введите координаты точки B: '))
    B.append(number)    

import math
distance = math.sqrt(((A[0]-B[0])**2)+((A[1]-B[1])**2))

print("Расстояние между точками = ", '%.2f' % distance)  
