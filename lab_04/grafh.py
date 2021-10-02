import matplotlib.pyplot as plt

# import matplotlib.ticker as ticker

count = [1, 4, 8, 16,  32]

trace = [14021.29 for i in range(5)]
paralltrace = [14021.29, 13848.28, 8434.71, 12263.14, 7054.88]

fig, ax = plt.subplots()

# Что бы шаг по оси x был не стандартным,
# А массивом count.
plt.xticks(count)

ax.plot(count, trace, label="Обычная сортировка")

ax.plot(count, paralltrace, label="Параллельноая сортировка")

ax.scatter(count, paralltrace, c='deeppink')

ax.scatter([1, 32], [14021.29, 14021.29], c='blue')


ax.legend()
ax.grid()
ax.set_xlabel('Количество потоков')
ax.set_ylabel('Время (мс)')

plt.show()




# res1000 = [ 237.51, 132.10, 26.69, 38.80,12.48]
# res10000 = [661.43, 567.41, 423.90, 445.27, 493.91]
# res50000 = [14021.29, 13848.28, 8434.71, 12263.14, 7054.88]


# n1 = 100
# n2 = 1000
# h = 200
# len_arr = [100, 5100, 10100, 15100, 20100, 25100, 30100, 35100, 40100, 45100, 50100, 55100, 60100, 65100, 70100, 75100, 80100, 85100, 90100, 95100]
# result1 = [0, 139, 310, 797, 1197, 1864, 2715, 3760, 4967, 6412, 8021, 10678, 12962, 14903, 18852, 20088, 24559, 27746, 31515, 34317]
# result2 = [70, 31, 126, 222, 381, 581, 847, 1151, 1512, 1961, 2705, 3329, 3671, 4560, 5289, 6051, 6662, 8319, 10436, 11946]
#
#
# fig1 = plt.figure(figsize=(10, 7))
# plot = fig1.add_subplot()
# plot.plot(len_arr, result1, label = "Последовательный")
# plot.plot(len_arr, result2, label="Параллельный")
# plt.legend()
# plt.grid()
# plt.title("Временные характеристики")
# plt.ylabel("Затраченное время (мск)")
# plt.xlabel("Длина")
#
# plt.show()