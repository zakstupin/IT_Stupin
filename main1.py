money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
collectors = 0
while money_capital + collectors > 0:
    collectors = collectors + (salary - spend)
    spend = spend * (1 + increase)
    count+=1
count-=1 # Потому что в конце последнего успешного цикла мы посчитали count, который привел к невыполнению условия
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
