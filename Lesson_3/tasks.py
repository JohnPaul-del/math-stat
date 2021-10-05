from math import factorial as f

import numpy as np


def math_choice(n, k):
    return f(n) / (f(k) * f(n - k))


"""
TASK 1
Даны значения зарплат из выборки выпускников: 
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, 
среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""

s_array = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
# Mean
average = s_array.sum() / s_array.size

# Mean Square
square_average = (np.sum((s_array - average) ** 2) / s_array.size) ** 0.5

# Biased variance
b_variance = np.sum((s_array - average) ** 2) / s_array.size

# Unbiased variance
ub_variance = np.sum((s_array - average) ** 2) / (s_array.size - 1)

print(f"{'.'*20} Task 1 {'.'*20}\n"
      f"Mean: {average}\n"
      f"Mean square: {square_average}\n"
      f"Biased variance: {b_variance}\n"
      f"Unbiased variance: {ub_variance}\n")

"""
TASK 2
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
"""

# Ver.1 Basket 1 = 0 white, Basket 2 = 3 white
basket_1 = (math_choice(5, 0) * math_choice(3, 2)) / math_choice(8, 2)
basket_2 = (math_choice(5, 3) * math_choice(7, 1)) / math_choice(12, 4)
chance_1 = basket_1 * basket_2

# Ver.1 Basket 1 = 1 white, Basket 2 = 2 white
basket_1 = (math_choice(5, 1) * math_choice(3, 1)) / math_choice(8, 2)
basket_2 = (math_choice(5, 2) * math_choice(7, 2)) / math_choice(12, 4)
chance_2 = basket_1 * basket_2

# Ver.1 Basket 1 = 2 white, Basket 2 = 1 white
basket_1 = (math_choice(5, 2) * math_choice(3, 0)) / math_choice(8, 2)
basket_2 = (math_choice(5, 1) * math_choice(7, 3)) / math_choice(12, 4)
chance_3 = basket_1 * basket_2

total = chance_1 + chance_2 + chance_3
print(f"{'.'*20} Task 2 {'.'*20}\n"
      f"3 balls: {total}\n")

"""
TASK 3
На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
Найти вероятность того, что выстрел произведен: 
a). первым спортсменом 
б). вторым спортсменом 
в). третьим спортсменом.
"""
shot_chance = 1 / 3 * 0.9 + 1 / 3 * 0.8 + 1 / 3 * 0.6
shot_1 = (1 / 3 * 0.9) / shot_chance
shot_2 = (1 / 3 * 0.8) / shot_chance
shot_3 = (1 / 3 * 0.6) / shot_chance

print(f"{'.'*20} Task 3 {'.'*20}\n"
      f"Good shot by #1: {shot_1}\n"
      f"Good shot by #2: {shot_2}\n"
      f"Good shot by #3: {shot_3}\n")
"""
TASK 4
В университет на факультеты A и B поступило равное количество студентов, 
а на факультет C студентов поступило столько же, сколько на A и B вместе. 
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
Студент сдал первую сессию. Какова вероятность, что он учится: 
a). на факультете A 
б). на факультете B 
в). на факультете C?
"""
good_session = 1 / 4 * 0.8 + 1 / 4 * 0.7 + 2 / 4 * 0.9
faculty_1 = (1 / 4 * 0.8) / good_session
faculty_2 = (1 / 4 * 0.7) / good_session
faculty_3 = (2 / 4 * 0.9) / good_session

print(f"{'.'*20} Task 4 {'.'*20}\n"
      f"Faculty A: {faculty_1}\n"
      f"Faculty B: {faculty_2}\n"
      f"Faculty C: {faculty_3}\n")

"""
TASK 5
Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
для второй - 0.2, для третьей - 0.25. 
Какова вероятность того, что в первый месяц выйдут из строя: 
а). все детали 
б). только две детали 
в). хотя бы одна деталь 
г). от одной до двух деталей?
"""
bad_news = 0.1 * 0.2 * 0.25
two_broken = 0.1 * 0.2 * (1 - 0.25) + 0.1 * (1 - 0.2) * 0.25 + (1 - 0.1) * 0.2 * 0.25
one_broken = 1 - (1 - 0.1) * (1 - 0.2) * (1 - 0.25)
broken_1_2 = 1 - bad_news - (1 - 0.1) * (1 - 0.2) * (1 - 0.25)

print(f"{'.'*20} Task 5 {'.'*20}\n"
      f"All broken: {bad_news}\n"
      f"Two are broken: {two_broken}\n"
      f"One is broken: {one_broken}\n"
      f"One or two are broken: {broken_1_2}\n")

"""
RESULTS 
.................... Task 1 ....................
Mean: 65.3
Mean square: 30.823854398825596
Biased variance: 950.11
Unbiased variance: 1000.1157894736842

.................... Task 2 ....................
3 balls: 0.3686868686868687

.................... Task 3 ....................
Good shot by #1: 0.391304347826087
Good shot by #2: 0.3478260869565218
Good shot by #3: 0.2608695652173913

.................... Task 4 ....................
Faculty A: 0.24242424242424246
Faculty B: 0.21212121212121213
Faculty C: 0.5454545454545455

.................... Task 5 ....................
All broken: 0.005000000000000001
Two are broken: 0.08000000000000002
One is broken: 0.45999999999999996
One or two are broken: 0.45499999999999996
"""
