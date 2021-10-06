# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет
# процент (годовой) - 15%
# ежемесячная капитализация
#
#
# Вычислить сумму на счету в конце указанного срока.
# S=P*(1+j/m)mn
#
# где j/m – ставка за период, исчисленная на основе базовой (номинальной ставки j) и числа раз начислений процентов в году (m);
#
# mn – число процентных периодов, исчисленное на основе числа раз начислений процентов в году (m) и срока финансовой операции в годах (n) или не в годах (t/Y).
#
# P – первоначальный капитал.
#
# S – наращенный капитал.


first_sum = int(input('Введите начальную сумму вклада:\n'))
srok = int(input('Введите срок вклада(в годах):\n'))
procent = int(input('Введите процент годовой:\n'))
vid_kapital = input('Введите вариант капитализации(y-год или m-месяц):\n')


if vid_kapital =='m':
    itog_sum = first_sum * (1 + (procent/100)/12)**(srok*12)
    print(f'Итоговая сумма через {srok} лет:\n{round(itog_sum)}')
    print(f'Радуйтесь вы заработали:\n{round(itog_sum)-first_sum}')

else:
    itog_sum = first_sum * (1 + (procent / 100)) ** srok
    print(f'Итоговая сумма через {srok} лет:\n{round(itog_sum)}')
    print(f'Радуйтесь вы заработали:\n{round(itog_sum) - first_sum}')