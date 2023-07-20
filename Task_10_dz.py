# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите кол-во монеток: '))
orel = reshka = 0
for i in range(n):
    a = int(input('Введите положение монетки, где орел - 1, решка - 0: '))
    if a == 0:
        reshka += 1
    else:
        orel += 1
if orel > reshka:
    print(f'Переверните {reshka} монет с решки на орла, их меньше всего.')
elif orel == reshka:
    print(f'Монет с решками и орлами одинаково по {reshka}, перевернуть можно на любую сторону.')
else:
    print (f'Переверните {orel} монет с орла на решку, их меньше всего.')