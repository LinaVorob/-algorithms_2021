"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
"""
Задание 2.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
"""
#first algorithm
def min_val_first(lst): #O(n^2)
    for i in range(len(lst)-1):#O(N)
        for j in range(len(lst)-i-1): #O(N)
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] #O(2)
    return lst[0]

#second algorithm
def min_val_second(lst): #O(N)
    min_value = lst[0] #O(1)
    for ind in lst[1:]: #O(n)
        if ind < min_value:
            min_value = ind #O(1)
    return min_value #O(1)
    
lst = [4,8,55,9,3,10,12,52,24,13]
print(f'Первый алгоритм: {min_val_first(lst)}. Второй алгоритм: {min_val_second(lst)}')

