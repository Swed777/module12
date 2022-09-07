print('Задача 3. Апгрейд калькулятора')
print()
print('--------------------------')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.

def summ_unit(number):
  sum = 0
  while (number != 0):
    sum = sum + number % 10
    number = number // 10
  print("Сумма цифр числа равна: ", sum)

def max_unit(number):
  tmp_unit = 0
  max_unit = 0
  while (number != 0):
    tmp_unit = number % 10
    if tmp_unit > max_unit:
       max_unit = tmp_unit
    number = number // 10
  print("Максимальная цифра числа равна: ", max_unit)
  
def min_unit(number):
  tmp_unit = 0
  min_unit = number
  while (number != 0):
    tmp_unit = number % 10
    if tmp_unit < min_unit:
       min_unit = tmp_unit
    number = number // 10
  print("Минимальная цифра числа равна: ", min_unit)


while True:
  number = int(input('Введите число: '))
  print()
  digit = input('Что с ним нужно сделать? 1. - вывести сумму цифр 2. - вывести максимальную цифру, 3. - вывести минимальную цифру ')
  if digit == '1':
    summ_unit(number)
  elif digit == '2':
    max_unit(number)
  elif digit == '3':
    min_unit(number)
  else:
    print('Введите цифры 1, 2 или 3')





print()
print('--------------------------') 