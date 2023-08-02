# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Вариант 1. Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой возможность комплексных решений. Можно игнорировать то, что получаться рациональные решения вместо натуральных.
# Для вычисления квадратного корня используйте возведение в степень 0.5 или
# (*) Усложнение для варианта 1. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.
# Вариант 2. Решить эту задачу можно "перебором значений" в цикле

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# if(num2 == (num1 ** 2)):
#     x = num2 - num1 / 2
#     y = num2 + num1 ** 0.5

# print(f"Первое чилсо равно {x}")
# print(f"Второе чилсо равно {y}")

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for x in range(1, 1001):
    y = s - x
    if x * y == p:
        print(x, y)
        break