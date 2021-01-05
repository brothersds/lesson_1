# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

user_profit = int(input('Введите значение выручки фирмы: '))
user_cost = int(input('Введите значение издержек фирмы: '))

if user_profit > user_cost:
    print('Фирма работает с прибылью: ', '{0:10.2f}'.format(user_profit - user_cost))
    user_margin = 100 * ((user_profit - user_cost) / user_profit)
    print('Рентабельность выручки: ', '{0:10.2f}'.format(user_margin), '%')
    number_employees = int(input('Введите количество сотрудников: '))
    employees_profit = (user_profit - user_cost) / number_employees
    print('Прибыль фирмы в расчете на одного сотрудника: ', '{0:10.2f}'.format(employees_profit))

else:
    print('Фирма работает с убытком: ')
