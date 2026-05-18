import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data.copy())
    end_time = time.time()
    return end_time - start_time

sizes = [10, 100, 1000]
results = {}

for size in sizes:
    test_data = [random.randint(1, 1000) for _ in range(size)]
    merge_time = measure_time(merge_sort, test_data)
    bubble_time = measure_time(bubble_sort, test_data)
    results[size] = {
        'merge_sort': merge_time,
        'bubble_sort': bubble_time
    }

print("\nСравнение времени выполнения сортировок:")
print("=" * 50)
print(f"{'Размер':<10} {'MergeSort (сек)':<20} {'BubbleSort (сек)':<20}")
print("-" * 50)
for size, times in results.items():
    print(f"{size:<10} {times['merge_sort']:<20.6f} {times['bubble_sort']:<20.6f}")
