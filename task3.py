#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def enter_parametr_array():
    number=int(input('Введите количество элементов N-> '))
    min_value=int(input('Введите мин значение min-> '))
    max_value=int(input('Введите максимальное значение max-> '))
    return(number,min_value,max_value)

def fill_ramdom_array():
    list_param=enter_parametr_array()
    list_values=[0]*list_param[0]
    for i in range(list_param[0]):
        list_values[i]=int(random.randint(list_param[1],list_param[2]))
    return list_values
import random

list_values=fill_ramdom_array()
print(list_values, end=' ')
print()
list_res=[]
for i in range(len(list_values)):
    j=0
    flag=True
    while j<len(list_values) and flag:
        if list_values[i]==list_values[j] and i!=j : flag=False
        j+=1
    if flag: list_res.append(list_values[i])
print(list_res, end=' ')
print()