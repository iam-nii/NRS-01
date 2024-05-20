import numpy as np
from scipy.interpolate import LinearNDInterpolator


def box_method(A1, A2, F, max_iter=100, tolerance=1e-6, jitter=1e-5):
    # Инициализация комплекса точек
    points = np.array(list(zip(A1, A2, F)))

    def centroid(points, exclude_index):
        # Вычисление центра тяжести комплекса точек, исключая одну
        filtered_points = np.delete(points, exclude_index, axis=0)
        return np.mean(filtered_points[:, :2], axis=0)

    def reflect(worst_point, centroid, alpha=1.3):
        # Отражение худшей точки относительно центра тяжести
        return centroid + alpha * (centroid - worst_point[:2])

    for iteration in range(max_iter):
        # Добавление случайного шума для избежания ошибок в вычислениях
        points[:, :2] += np.random.uniform(-jitter, jitter, size=points[:, :2].shape)

        # Сортировка точек по значениям целевой функции
        points = points[points[:, 2].argsort()]

        # Определение лучших и худших точек
        best = points[0]
        worst = points[-1]

        # Вычисление центра тяжести всех точек, кроме худшей
        c = centroid(points, -1)

        # Отражение худшей точки
        reflected_point = reflect(worst, c)

        # Интерполяция значения функции в отраженной точке
        interpolator = LinearNDInterpolator(points[:, :2], points[:, 2])
        reflected_value = interpolator(reflected_point)

        # Обработка случая, если отраженное значение выходит за пределы известных данных
        if np.isnan(reflected_value):
            reflected_value = worst[2]  # Если отражение выходит за известные границы, используем худшее значение

        # Сравнение отраженной точки с лучшей точкой
        if reflected_value < best[2]:
            # Замена худшей точки на отраженную точку
            points[-1] = np.append(reflected_point, reflected_value)
        else:
            # Если отражение не улучшает результат, сжатие к лучшей точке
            for i in range(1, len(points)):
                points[i][:2] = best[:2] + 0.5 * (points[i][:2] - best[:2])

        # Проверка на сходимость
        if np.std(points[:, 2]) < tolerance:
            break

    # После сходимости лучшая точка должна быть минимумом, а худшая - максимумом
    points = points[points[:, 2].argsort()]
    min_point = points[0]
    max_point = points[-1]

    return [[min_point[0], min_point[1], min_point[2]], [max_point[0], max_point[1], max_point[2]]]


# Пример использования
A1 = np.random.rand(20) * 10  # Случайные значения для A1 от 0 до 10
A2 = np.random.rand(20) * 10  # Случайные значения для A2 от 0 до 10
F = A1 ** 2 + A2 ** 2  # Пример целевой функции: f(a1, a2) = a1^2 + a2^2

min_extreme, max_extreme = box_method(A1, A2, F)

print(f"Минимальное экстремум: {min_extreme}")
print(f"Максимальное экстремум: {max_extreme}")
