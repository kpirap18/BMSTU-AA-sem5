# import matplotlib.pyplot as plt

# # import matplotlib.ticker as ticker

# count = [3, 4, 5, 6, 7, 8, 9, 10]

# usual_alg = [991211, 1005398, 1145161, 1395963, 3142151, 4743608, 42384948, 162236576]
# ant_alg =   [960372, 1000882, 1087988, 1320744, 1574520, 1961224, 10383369, 20311214]

# fig, ax = plt.subplots()


# # Что бы шаг по оси x был не стандартным,
# # А массивом count.
# plt.xticks(count)

# ax.plot(count, usual_alg, label="Алгоритм полного перебора")

# ax.plot(count, ant_alg, label="Муравьиный алгоритм")

# ax.scatter(count, ant_alg, c='deeppink')
# ax.scatter(count, usual_alg, c='blue')

# ax.legend()
# ax.grid()
# ax.set_xlabel('Кол-во вершин')
# ax.set_ylabel('Время (такт)')

# plt.show()

# f = open("res.txt", "r")
# ff = open("res2.txt", "w")



# for i in range(686):
#     a = f.readline()
#     a = a[:len(a) - 1]
#     aa = a + ' \\\\\n'
#     ff.write(aa)
# f.close()
# ff.close()

print(f" select t.tourid, t.nametour \
from packages.tours t join location1.cities c on t.cityid = c.cityid \
join location1.countries c2 on c.countryid = c2.countryid")