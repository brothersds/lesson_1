# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите целое положительное число: '))
task_number = []
while user_number > 10:
    task_number.append(user_number % 10)
    user_number //= 10
task_answer = max(task_number)
print('Самая большая цифра в числе: ', task_answer)
