# Петя задумывает 2 числа, Катя должна отгадать их. При этом 
# Петя дает подсказку: называет сумму этих чисел и произведение. 
# Найти задуманные числа

print('Введите сумму чисел: ')
sum = int(input())
print('Введите произведение чисел: ')
proiz = int(input())
# 5 6
for i in range(sum):
    if i * (sum - i) == proiz:
        x = i
        y = sum - i
print(x, y)
