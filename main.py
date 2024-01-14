
# в императивном стиле
def bubble_sort_desc(numbers):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Декларативный стиль
def declarative_sort_desc(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_desc(numbers)
print("Отсортированный список в порядке убывания:", numbers)

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = declarative_sort_desc(numbers)
print("Отсортированный список в порядке убывания:", sorted_numbers)





