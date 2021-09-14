import sys
import string
import threading
import random
from time import time, thread_time, process_time
from copy import deepcopy


def shaker_sort(arr):
    length = len(arr)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):
        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (arr[i] > arr[i + 1]):
                # обмен элементов
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False
        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (arr[i] > arr[i + 1]):
                # обмен элементов
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start_index = start_index + 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def array_alg(func):
    arr = list(map(int, input("Введите массив: ").split()))
    arr = func(arr)
    print("Отсортирваный массив", arr)

def main():
    do_start = True

    while (do_start):
        command = input("\n\nМЕНЮ: \n"
                        "\t 0. Выход\n"
                        "\t 1. Сортировка Шейкер\n"
                        "\t 2. Сортировка вставками\n"
                        "\t 3. Сортировка выбором\n"
                        "\t 4. Замер времени (длина слов от 1 до 10)\n"
                        "\t Выбор: ")
        if (command == "1"):
            array_alg(shaker_sort)
        elif (command == "2"):
            array_alg(insertion_sort)
        elif (command == "3"):
            array_alg(selection_sort)
        elif (command == "4"):
            arr = list(map(int, input("Введите массив: ").split()))

            arr1 = deepcopy(arr)

            start = process_time()
            for i in range(100000):
                arr1 = deepcopy(arr)
                shaker_sort(arr1)
            end = process_time()
            sheker_time = (end - start) / 100000

            start = process_time()
            for i in range(100000):
                arr1 = deepcopy(arr)
                insertion_sort(arr1)
            end = process_time()
            insert_time = (end - start) / 100000

            start = process_time()
            for i in range(100000):
                arr1 = deepcopy(arr)
                selection_sort(arr1)
            end = process_time()
            selecr_time = (end - start) / 100000

            print("Массив отсортированный сортировкой-Шейкер ", arr1)
            print("Время в мкс (сортировкой-Шейкер) ", sheker_time * 1000000)
            print("Массив отсортированный сортировкой вставками ", arr1)
            print("Время в мкс (сортировкой вставками) ", insert_time * 1000000)
            print("Массив отсортированный сортировкой выбором ", arr1)
            print('Время в мкс (сортировкой выбором)', selecr_time * 1000000)
        else:
            do_start = False


if __name__ == "__main__":
    main()