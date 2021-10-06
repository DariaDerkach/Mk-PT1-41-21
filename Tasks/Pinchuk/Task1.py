"""
Депозит:
начальная сумма - 20000 BYN
срок - 5 лет
процент (годовой) - 15%
ежемесячная капитализация

Вычислить сумму на счету в конце указанного срока.
"""

summa = 20000  # BYN
x = 15 / 12  # узнаю ежемесячный процент
x1 = x / 100 + 1  # ежемесячный множитель суммы ("100" - это проценты, а "1" не знаю как объяснить)
m = 5 * 12  # количество месяцев за весь срок
result = summa
acc = []
for i in range(1, m+1):
    result = result * x1
    acc.append(round(result, 2))
print(f'Сумма на счету в конце срока: {round(result, 2)}')
print(f'Сумма депозита в конце каждого месяца: {acc}')
