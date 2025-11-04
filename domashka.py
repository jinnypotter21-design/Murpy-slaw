import random
#задача2

min_val = int(input("Введите минимальное значение диапазона: "))
max_val = int(input("Введите максимальное значение диапазона: "))
count = int(input("Сколько чисел сгенерировать? "))


numbers = []
for i in range(count):
    numbers.append(random.randint(min_val, max_val))


actual_min = min(numbers)
actual_max = max(numbers)


negatives = 0
positives = 0
zeros = 0

for i in range(len(numbers)):
    num = numbers[i]
    if num < 0:
        negatives += 1
    elif num > 0:
        positives += 1
    else:
        zeros += 1


print("Минимальный элемент: " , actual_min )
print("Максимальный элемент: ", actual_max)
print("Количество отрицательных: ", negatives)
print("Количество положительных: " , positives)
print("Количество нулей: ", zeros)



#задача1
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
        result = num1 / num2
        print(result)
else:
    print("Вы ввели неправильную операцию!")

#jvjubnt
#zytpyf.rfrgjkmpjdfnmczubn[f,jv
#vytdsytckbvjpu
#zk,k.dfibgfhs
#https://static.tildacdn.com/tild3862-3432-4562-a662-666362303333/__3.pngмемчик