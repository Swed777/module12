print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(number, letter):
  count_n = 0
  count_l = 0
  for i in text:
    if i == number:
      count_n += 1
    elif i == letter:
      count_l += 1
  print(f'Количество цифр {number}: {count_n}')
  print(f'Количество букв {letter}: {count_l}')


text   = input('Введите текст: ')
number = input('Какую цифру ищем?: ')
letter = input('Какую букву ищем?: ')
print()
count_letters(number, letter)

# Вопрос от Игоря - верно ли выбран алгоритм выделения функии? Может, в функцию нужно было заложить какой-то другой расчет?


