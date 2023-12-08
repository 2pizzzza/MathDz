import matplotlib.pyplot as plt
from statistics import mean, variance, median
from collections import Counter


data = [-0.028, -0.698, -0.033, -1.084, -0.157, -0.402, -0.077, 2.043, -0.187, -0.663,
       1.143, 1.57, -1.86, 1.445, -1.499, -1.78, -0.719, -0.314, 0.67, -0.349, -1.99,
       -0.128, 0.341, 0.837, 1.84, -0.832, 0.066, -1.528, -3.215, 1.715, -0.646, -2.264,
       -2.064, 0.173, 0.519, -1.198, 1.868, 0.614, 1.456, 0.48, -1.622, 1.092, -1.505,
       -0.134, -0.489, -1.258, -2.129, 0.318, 0.672, -0.359]


plt.hist(data, bins=15, edgecolor='black')
plt.title('Гистограмма значений')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()


sample_mean = mean(data)
print(f'Выборочное среднее: {sample_mean:.3f}')


sample_variance = variance(data)
print(f'Выборочная дисперсия: {sample_variance:.3f}')


sample_median = median(data)
print(f'Выборочная медиана: {sample_median}')


counter = Counter(data)
most_common = counter.most_common(1)


if most_common[0][1] == 1:
   print('Мода не найдена (все значения уникальны)')
else:
   sample_mode = most_common[0][0]
   print(f'Выборочная мода: {sample_mode}')