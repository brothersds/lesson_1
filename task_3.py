# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введите число n: '))

user_number_x2 = int(2 * str(user_number))
user_number_x3 = int(3 * str(user_number))
task_answer = user_number + user_number_x2 + user_number_x3

print('Сумма чисел n + nn + nnn: ', task_answer)
