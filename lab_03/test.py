import sys
from time import process_time
import random
import numpy as np  # np.array([random.randint(0, 1000) for i in range(100)])
import copy
import matplotlib.pyplot as plt

from main import *


def get_random_array(n):
    array = []

    for i in range(n):
        array.append(random.randint(0, 20000))

    return array


def get_best_array(n):
    array = []

    for i in range(n):
        array.append(i)

    return array


def get_worst_array(n):
    array = []

    for i in range(n):
        array.append(n - i)

    return array


def get_calc_time(func, arr):
    t2 = process_time()
    func(arr)
    t1 = process_time() - t2

    return t1


def measure_time(get_array, n1, n2, st, it):
    t_bubble = []
    t_insert = []
    t_select = []

    for n in range(n1, n2, st):
        # print(n, ' ', time.process_time())
        t = 0

        for i in range(it):
            arr = get_array(n)
            t += get_calc_time(shaker_sort, arr)

        t_bubble.append(t / it * 1000000)
        t = 0

        for i in range(it):
            arr = get_array(n)
            t += get_calc_time(insertion_sort, arr)

        t_insert.append(t / it * 1000000)
        t = 0

        for i in range(it):
            arr = get_array(n)
            t += get_calc_time(selection_sort, arr)

        t_select.append(t / it * 1000000)

    return (t_bubble, t_insert, t_select)



def time_all():
    nu = [100, 200, 300, 400, 500, 600, 1000, 2000, 2500]
    t_bubble = []
    t_insert = []
    t_select = []
    it = 100

    for n in nu:
        print(n)
        t = 0

        for i in range(it):
            arr = get_worst_array(n)
            t += get_calc_time(shaker_sort, arr)

        t_bubble.append(t / it * 1000000)
        t = 0

        for i in range(it):
            arr = get_worst_array(n)
            t += get_calc_time(insertion_sort, arr)

        t_insert.append(t / it * 1000000)
        t = 0

        for i in range(it):
            arr = get_worst_array(n)
            t += get_calc_time(selection_sort, arr)

        t_select.append(t / it * 1000000)

    print(nu)
    print(t_bubble)
    print(t_insert)
    print(t_select)


# time_all()

n1 = 100
n2 = 1000
h = 200
len_arr = [100, 300, 500, 700, 900]
result1 = measure_time(get_best_array, n1, n2 + 1, h, 100)
result2 = measure_time(get_worst_array, n1, n2 + 1, h, 100)
result3 = measure_time(get_random_array, n1, n2 + 1, h, 100)


fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
plot.plot(len_arr, result1[0], label = "Сортировка Шейкер")
plot.plot(len_arr, result1[1], label="Сортировка вставками")
plot.plot(len_arr, result1[2], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировок")
plt.ylabel("Затраченное время (мск)")
plt.xlabel("Длина")
print("res1 отсортированные данные", result1)

fig2 = plt.figure(figsize=(10, 7))
plot = fig2.add_subplot()
plot.plot(len_arr, result2[0], label = "Сортировка Шейкер")
plot.plot(len_arr, result2[1], label="Сортировка вставками")
plot.plot(len_arr, result2[2], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировок")
plt.ylabel("Затраченное время (мск)")
plt.xlabel("Длина")
print("res2 обратные порядок", result2)

fig3 = plt.figure(figsize=(10, 7))
plot = fig3.add_subplot()
plot.plot(len_arr, result3[0], label = "Сортировка Шейкер")
plot.plot(len_arr, result3[2], label="Сортировка вставками")
plot.plot(len_arr, result3[1], label="Сортировка выбором")
plt.legend()
plt.grid()
plt.title("Временные характеристики алгоритмов сортировок")
plt.ylabel("Затраченное время (мск)")
plt.xlabel("Длина")
print("res3 слйчайный порядок", result3)

plt.show()
