# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_answer = int(input('Введите время в секундах: '))

task_hour = user_answer // 3600
task_minute = (user_answer % 3600) // 60
task_second = (user_answer % 3600) % 60

max_width = 2
print(f'{task_hour:0{max_width}}:{task_minute:0{max_width}}:{task_second:0{max_width}}')
