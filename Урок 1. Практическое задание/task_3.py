"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
#first decision
'''Сложность решения: O(N log N)'''
def top_company(dict_com):
    sorted_dict = sorted(dict_com.values()) #O(N log N)
    empty_dict = {} #O(1)
    for i in range(1, 4):
        for key in dict_com.keys(): #O(1)
            if dict_com[key] == sorted_dict[-i]:#O(1)
                empty_dict[key] = sorted_dict[-i] #O(1)
    return empty_dict
company = {'A': 152324, 'B': 12311, 'C': 321721, 'D': 8211, 'E': 93181, 'F': 41356}
print(top_company(company))

#second decision
'''Сложность решения: O(n)'''
def the_richest_company(dict_com):
    new_dict = list(dict_com.values())#O(n)
    len_list = len(new_dict) #O(1)
    for i in range(len_list-3): #O(1)
        new_dict.pop(new_dict.index(min(new_dict))) #O(n)+O(n)+O(1)
    final_dict = {} #O(1)
    for i in dict_com.keys(): #O(1)
        if dict_com[i] in new_dict: #O(n)
            final_dict[i] = dict_com[i] #O(1)
    return final_dict
company = {'A': 152324, 'B': 12311, 'C': 321721, 'D': 8211, 'E': 93181, 'F': 41356}
print(the_richest_company(company))

'''В результате получилось, что первое решение эффективнее, т.к. в основном использовались функции словаря. 
Во втором решении использовались в основном функции и методы списка'''

