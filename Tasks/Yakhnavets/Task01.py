start=int(input("введите сумму депозита\n"))
percent=int(input("введите годовой процент\n"))
years=int(input("Срок\n"))
Sper=(1+(percent/100)/12)**(years*12)
print(Sper*start)
