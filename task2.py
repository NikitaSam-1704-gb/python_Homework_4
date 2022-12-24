# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('Найти ряд простых множителей числа N')
number=int(input('Введите число N-> '))
list_rem=[]
while number>1:
    i=2
    flag=True
    while i <= number and flag:
        rem=number/i
        if rem%1==0:
            list_rem.append(i)
            if rem==1:
                list_rem.append(int(rem))
            flag=False
            number=rem
        i+=1
print(list_rem)