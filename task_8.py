print('Задача 8. НОД')
print('----------------------')
#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def max_n(a,b):
  if a < b :
    c = a
    a = b
    b = c
  return

def nod(a, b):  
  remain = a % b
  if remain == 0:
    print('Наибольший общий делитель = ', b)
  else:
    a = b
    b = remain
    nod(a, b)
    
a = int(input("Введите первое число: "))  
b = int(input("Введите второе число: "))
nod(a,b)

print('----------------------')