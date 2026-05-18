def merge_sort(arr):
    """
    Реализация сортировки слиянием.
    Возвращает новый отсортированный список.
    """
    # Базовый случай: если список содержит 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем список на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Сливаем отсортированные половины
    return merge(left_half, right_half)

def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных списков.
    """
    result = []
    i = j = 0

    # Сравниваем элементы из обоих списков и добавляем меньший в результат
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левого списка, если они есть
    while i < len(left):
        result.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правого списка, если они есть
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Пример использования сортировки слиянием
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(unsorted_list)
print(f"Исходный список: {unsorted_list}")
print(f"Отсортированный список: {sorted_list}")
