# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у
# пользователя любое число. В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
# указанному в условии ввода данных. Далее программа работает по следующему алгоритму:
#
# 1. Преобразование введённой последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем(для реализации сортировки определите функцию)
# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
# или равен этому числу.
#
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.
#
# Подсказка
#
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести
# соответствующее сообщение

data_list = [int(x) for x in input("Введите числа через пробел: ").split()]

def merge_sort(data_list):  # "разделяй"
    if len(data_list) < 2:  # если кусок массива равен 2,
        return data_list[:]  # выход из рекурсии
    else:
        middle = len(data_list) // 2  # ищем середину
        left = merge_sort(data_list[:middle])  # рекурсивно делим левую часть
        right = merge_sort(data_list[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(data_list))

def binary_search(data_list, num):
    left = 0
    right = len(data_list)
    sort_list = merge_sort(data_list)
    while (left <= right):

        mid = (left + right) // 2
        if sort_list[mid] < num and sort_list[mid+1] >= num:
            return f'Отсортированный список: {sort_list}'\
                f"\nБлижайшее наименьшее число: {sort_list[mid]}, его индекс: {mid}"
        elif sort_list[mid] == num:
            return f'Отсортированный список: {sort_list}'\
                f"\nБлижайшее наименьшее число: {sort_list[mid-1]}, его индекс: {mid-1}"
        elif sort_list[0] == num:
            return f'Число является начальным: {num}.'\
                   f'\nОтсортированный список: {sort_list}'
        elif sort_list[mid] > num:
            right = mid
        elif sort_list[mid] < num:
            left = mid+1
    return "Неккоректно произведена сортировка. Попробуйте снова."

while True:
    try:
        num = int(input("Введите число от 1 до 999: "))
        if num < 0 or num > 999:
            raise Exception
        break
    except ValueError:
        print("Необходимо ввести целое число")
    except Exception:
        print("Число не соответствует диапозону")

print(binary_search(data_list, num))