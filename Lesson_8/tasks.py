import numpy as np

"""
Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, 
хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов: 
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
powerlifter = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
f_mean = football.mean()
h_mean = hockey.mean()
p_mean = powerlifter.mean()
f_len = len(football)
h_len = len(hockey)
p_len = len(powerlifter)
n = f_len + h_len + p_len
general = np.hstack((football, hockey, powerlifter))
general_mean = np.mean(general)
general_sqrt = np.sum((general - general_mean) ** 2)
group_sqrt = ((f_mean - general_mean) ** 2) * f_len + \
             ((h_mean - general_mean) ** 2) * h_len + \
             ((p_mean - general_mean) ** 2) * p_len
residual_sqrt = general_sqrt - group_sqrt
general_sigma = general_sqrt / (n - 1)
factorial_sigma = group_sqrt / (3 - 1)
residual_sigma = residual_sqrt / (n - 3)

F_h = factorial_sigma / residual_sigma
res = group_sqrt / general_sqrt
F_kr = 3.385

print(f"{'.'*20} Task {'.'*20}\n"
      f"Football average: {f_mean}\n"
      f"Hockey average: {h_mean}\n"
      f"Powerlifter average: {p_mean}\n"
      f"General average: {general_mean}\n"
      f"Sqrt sum general: {general_sqrt}\n"
      f"Sqrt sum group: {group_sqrt}\n"
      f"Residual sqrt: {residual_sqrt}\n"
      f"General sigma: {general_sigma}\n"
      f"Factorial sigma: {factorial_sigma}\n"
      f"Residual sigma: {residual_sigma}\n"
      f"There are differences, because {F_kr} < {F_h}")

"""
Result

.................... Task ....................
Football average: 179.125
Hockey average: 178.66666666666666
Powerlifter average: 172.72727272727272
General average: 176.46428571428572
Sqrt sum general: 830.9642857142854
Sqrt sum group: 253.9074675324678
Residual sqrt: 577.0568181818177
General sigma: 30.776455026455015
Factorial sigma: 126.9537337662339
Residual sigma: 23.082272727272706
There are differences, because 3.385 < 5.5000534508126036
"""
