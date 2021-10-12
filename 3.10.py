
print('#3.10')
list=['1', '5', '4', '3', '2']
print (list)
messege11 = f'Вам нравится цифра {list[0]}.'
print(messege11)
deleted=list.pop(1)
print('Число '+deleted+' было удалено\n')
print('удалил 4-й элемент из списка:')
del list[3]
print (list)
print('отсортированый список:')
print(sorted(list)) 
print(list) 
print('обратный:')
list.reverse()
print(list) 
list.reverse()
print('отсортировано по списку:')
list.sort()
print(list) 
print('отсортированый и обратный:')
list.sort(reverse=1)
print(list)


 

