import matplotlib.pyplot as plt
from statistics import mean, variance, median
from collections import Counter

data = [2.316, 2.249, 1.829, 1.547, 2.294, 2.151, 1.066, 2.793, 2.716, 3.044,
        2.811, 2.617, 1.755, 1.914, 2.685, 2.791, 2.358, 1.789, 1.844, 2.136,
        2.864, 3.958, 2.069, 2.565, 2.557, 3.891, 3.479, -0.294, 2.662, 1.559,
        1.526, 2.089, 1.301, 2.347, 1.125, 3.9, -0.726, 2.87, 4.179, 3.085, 3.176,
        1.029, 0.424, 2.464, 3.474, 3.165, 1.237, 2.509, 2.496,  1.198]

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
