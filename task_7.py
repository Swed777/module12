print('Задача 7. Опять?')
print('--------------------------')

# Вы снова встретились со своим старым другом, 
# который был безмерно благодарен вам за то,
# что вы помогли ему сдать задачу тому преподавателю.
# 
# Вот только друг всё равно выглядел довольно грустным. 
# Спросив в чём дело, друг взорвался эмоциями и рассказал,
# что теперь препод попросил написать функцию нахождения минимального числа
# без использования условного оператора, циклов и функции min. 
# 
# Конечно же, вы решили снова помочь бедняге.
# Напишите для него такую программу.

def minNumber(a, b):
  x = ((a + b) - abs(a - b)) / 2
  print ('Наименьшее число = ', int(x))

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

minNumber(a, b)



print()
print('--------------------------')
