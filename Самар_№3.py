x = int(input('Введите начальную целую цифру последовательного числового массива:  '))
y = int(input('Введите последнюю целую цифру последовательного числового массива:  '))
z = list(range(x, y + 1, 1))
d = []
print('Элементы массива кратные 3:  ')
for i in z:
    if i%3 == 0:
        d.append(i)
print(d)
input('Нажмите любую клавишу и ENTER для выхода из программы:  ')
