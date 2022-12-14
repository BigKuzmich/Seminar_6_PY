# Дан список, вывести отдельно буквы и цифры.
#
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '2', '3')

import methods as m

length = m.enter_num('Введите размер массива: ')
print('Сгенерированный массив: ')
lst = m.create_list(length)
print(lst)

print('Отсортированный массив: ')
print(m.separate_by_elements(lst))