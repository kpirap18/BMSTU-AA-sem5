import main
import string
import random
import time

import matplotlib.pyplot as plt

N = 100
y_time_lev_rec = []
y_time_lev_matrix_rec = []
y_time_lev_matrix = []
y_time_dlev = []

len_arr = []


def test(len):
    time_lev_rec = 0
    time_lev_matrix_rec = 0
    time_lev_matrix = 0
    time_dlev = 0

    for i in range(N):
        s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))
        s2 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))

        start = time.process_time()
        main.levenshtein_matrix(s1, s2, False)
        stop = time.process_time()

        time_lev_matrix += stop - start

        start = time.process_time()
        main.levenshtein_matrix_recursive(s1, s2, False)
        stop = time.process_time()

        time_lev_matrix_rec += stop - start

        start = time.process_time()
        main.levenshtein_recursive(s1, s2, False)
        stop = time.process_time()

        time_lev_rec += stop - start

        start = time.process_time()
        main.damerau_levenshtein_recursive(s1, s2, False)
        stop = time.process_time()

        time_dlev += stop - start

    len_arr.append(len)
    y_time_lev_rec.append((time_lev_rec / N) * 1000000)
    y_time_lev_matrix_rec.append((time_lev_matrix_rec / N) * 1000000)
    y_time_lev_matrix.append((time_lev_matrix / N) * 1000000)
    y_time_dlev.append((time_dlev / N) * 1000000)

    return (time_lev_matrix / N) * 1000000, (time_lev_matrix_rec / N) * 1000000, (time_lev_rec / N) * 1000000, (time_dlev / N) * 1000000


def print_results(count):
    time_lev_matrix, time_lev_matrix_rec, time_lev_rec, time_dlev = test(count)
    print("\n--------------------------------------------------------------------------------------")
    print("Время работы функции при n = : ", count)
    print("Матричный способ нахождения расстояния Левенштейна: ", "{0:.6f}".format(time_lev_matrix), "мкс")
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", "{0:.6f}".format(time_lev_matrix_rec), "мкс")
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", "{0:.6f}".format(time_lev_rec), "мкс")
    print("Нахождение расстояния Дамерау-Левенштейна c использования рекурсии: ", "{0:.6f}".format(time_dlev), "мкс")

    return

if __name__ == "__main__":
    for i in range(10):
       print_results(i)

    fig = plt.figure(figsize = (10, 7))
    plot = fig.add_subplot()
    plot.plot(len_arr, y_time_lev_rec, label = "Р-Левенштейна(рек)")
    # plot.plot(len_arr, y_time_lev_matrix_rec, label = "Р-Левенштейна(рек+кеш)")
    # plot.plot(len_arr, y_time_lev_matrix, label = "Р-Левенштейна(мат)")
    plot.plot(len_arr, y_time_dlev, label = "Р-Дамерау-Левенштейна")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов вычисления расстояния")
    plt.ylabel("Затраченное время (мск)")
    plt.xlabel("Длина (симболы")


    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    # plot.plot(len_arr, y_time_lev_rec, label = "Р-Левенштейна(рек)")
    plot.plot(len_arr, y_time_lev_matrix_rec, label = "Р-Левенштейна(рек+кеш)")
    plot.plot(len_arr, y_time_lev_matrix, label = "Р-Левенштейна(мат)")
    # plot.plot(len_arr, y_time_dlev, label = "Р-Дамерау-Левенштейна")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов вычисления расстояния")
    plt.ylabel("Затраченное время (мск)")
    plt.xlabel("Длина (симболы")
    plt.show()
