#Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

print('Вывод числа ПИ с заданной точностью')
accuracy_pi=int(input('Введите количетво знаков после запятой ->'))
lim=1
pi=(4/1-2/4-1/5-1/6)
i=0
while lim>10**(-accuracy_pi+1):
    i+=1
    lim=pi
    pi+=(1/16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    lim=pi-lim
pi=int(pi*10**(accuracy_pi))
print(pi/10**(accuracy_pi))