per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму:"))
per_val = list(per_cent.values())
depozit = (round((per_val[0]*money/100), 2), round((per_val[1]*money/100), 2),
           round((per_val[2]*money/100), 2), round((per_val[3]*money/100), 2))
print(depozit)
print("Максимальная сумма", (max(depozit)))
