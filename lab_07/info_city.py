from time import process_time, time
from copy import deepcopy
from matplotlib import pylab

class InfoCity(object):
	country = str()

	def __init__(self, country):
		self.country = country

	def __str__(self):
		return "country: {0}\n".format(self.country)

class Dictionary(object):
    data = dict()
    f = open('resBFS.txt', 'w')
    f1 = open('resBS.txt', 'w')
    f2 = open('resSS.txt', 'w')

    def __init__(self, file_name):
        #self.data = dict()
        self.LoadData(file_name)

    def __getitem__(self, key):
        return self.data.get(key)

    def LoadData(self, file_name):
        f = open(file_name, 'r')

        for line in f:
            array = line.split(',')
            key = array[1]
            self.data[key] = InfoCity(array[2])

        f.close()

    
    def sorting_by_keys(self):
        new_dict = dict()
        list_keys = list(self.data.keys())
        list_keys.sort()

        for i in list_keys:
            new_dict[i] = self.data[i]

        return new_dict

    def sorting_by_values(self, data):
        new_dict = dict()

        list_d = list(data.items())
        list_d.sort(key=lambda i: i[1], reverse=True)
        for elem in list_d:
            new_dict[elem[0]] = elem[1]

        return new_dict

    def segmentation(self):
        # Разбиваем по буквам алфавита и
        # Сортируем (по убыванию) по кол-ву элементов в каждой букве.
        count_dict = {i: 0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

        for key in self.data:
            #print(key, count_dict)
            count_dict[key[0]] += 1

        # Сортируем по убыванию значений.
        count_dict = self.sorting_by_values(count_dict)

        # Создаем новый словарь (он будет отсортирован
        # по убыванию кол-ва значений.
        new_dict = {i: dict() for i in count_dict}

        # Заполняем новый словарь.
        for key in self.data:
            new_dict[key[0]].update({key: self.data[key]})

        return new_dict

    def BruteForceSearch(self, key):
        k = 0
        kk = list(self.data.keys())
        for elem in self.data:
            k += 1
            if key == elem:
                self.f.write(f"{kk.index(key)},{key},{k}\n")
                return self.data[elem]
        return -1

    def BinarySearch(self, key, list_keys):
        l, r = 0, len(list_keys) - 1
        k = 0
        kk = list(self.data.keys())
        while l <= r:
            middle = (r + l) // 2  # (l + (r - l) // 2)
            elem = list_keys[middle]
            k += 1
            if elem == key:
                self.f1.write(f"{kk.index(key)},{key},{k}\n")
                return self.data[elem]
            elif elem < key:
                l = middle + 1

            else:
                r = middle - 1

        return -1

    def SegmentalSearch(self, key, new_dict):
        c = 0
        kk = list(self.data.keys())
        for k in new_dict:
            c += 1
            # Если нашли нужную букву
            if key[0] == k:
                # То начинаем искать.
                c += 1
                for elem in new_dict[k]:
                    if elem == key:
                        self.f2.write(f"{kk.index(key)},{key},{c}\n")
                        return new_dict[k][elem]
                # Если не нашли среди слов, которые были
                # На искомую букву, значит в словаре нет такого слова.
                return -1
        return -1


def get_time_search(f, data, key, all_k,  d):
    sum = 0
    for i in range(100):
        start = process_time()
        if (f == 1):
            data.BruteForceSearch(key)
        if (f == 2):
            data.BinarySearch(key, all_k)
        if (f == 3):
            data.SegmentalSearch(key, d)
        sum += (process_time() - start)
    return sum / 100


def test_time(data):
    time_simple = []
    time_bin = []
    time_combined = []

    x_11list = list(data.data.keys())
    x_list = [i for i in range(len(x_11list))]
    list_keys = list(data.data.keys())
    for i in list_keys:
        time_simple.append(get_time_search(1, data,i, 0, 0))

    new_dict = data.sorting_by_keys()
    list_keys = list(new_dict.keys())
    lk = list(data.data.keys())
    for i in lk:
        time_bin.append(get_time_search(2, data, i, list_keys, 0))

    new_dict = data.segmentation()
    lk = list(data.data.keys())
    for i in lk:
        time_combined.append(get_time_search(3, data, i, 0, new_dict))

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x_list, time_simple, 'r--', label='Полный перебор')
    pylab.plot(x_list, time_bin, color='yellow', label='Бинарный поиск')
    pylab.plot(x_list, time_combined, 'b-.', label='С помощью сегментов')
    pylab.legend(loc='upper left')
    pylab.show()

    x1_list = []
    time_simple1 = []
    time_bin1 = []
    time_combined1 = []

    for i in range(len(x_list)):
        if i % 15 == 0:
            x1_list.append(i)
            time_simple1.append(time_simple[i])
            time_bin1.append(time_bin[i])
            time_combined1.append(time_combined[i])

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x1_list, time_simple1, 'r--', label='Полный перебор')
    pylab.plot(x1_list, time_bin1, color='yellow', label='Бинарный поиск')
    pylab.plot(x1_list, time_combined1, 'b-.', label='С помощью сегментов')
    pylab.legend(loc='upper left')
    pylab.show()

    # print("\nАлгоритм перебором ")
    # print("Максимальное время выполнения = ", max(time_simple))
    # print("Минимальное время выполнения = ", min(time_simple))
    # print("Среднее время выполнения = ", sum(time_simple) / len(time_simple))

    # print("\nБинарный поиск ")
    # print("Максимальное время выполнения = ", max(time_bin))
    # print("Минимальное время выполнения = ", min(time_bin))
    # print("Среднее время выполнения = ", sum(time_bin) / len(time_bin))

    # print("\nКомбинированный алгоритм ")
    # print("Максимальное время выполнения = ", max(time_combined))
    # print("Минимальное время выполнения = ", min(time_combined))
    # print("Среднее время выполнения = ", sum(time_combined) / len(time_combined))


def main():
    data = Dictionary('info.csv')
    test_time(data)
    key = input('Словарь содержит следующую структуру\n \
    key - Город; value - Страна\n Введите ключ: ')

    if key == '':
        print('Ошибка при вводе ключа, пожалуйста, повторите ввод\n')
        key = input('Введите ключ: ')

    print("\nValue 1 (BFS):\n{0}\n".format(data.BruteForceSearch(key)))

    new_dict = data.sorting_by_keys()
    list_keys = list(new_dict.keys())
    print("\nValue 2 (BS):\n{0}\n".format(data.BinarySearch(key, list_keys)))

    new_dict = data.segmentation()
    print("\nValue 3 (SS):\n{0}\n".format(data.SegmentalSearch(key, new_dict)))

    list_keys = list(data.data.keys())
    for i in list_keys:
        data.BruteForceSearch(i)

    new_dict = data.sorting_by_keys()
    list_keys = list(new_dict.keys())
    lk = list(data.data.keys())
    for i in lk:
        data.BinarySearch(i,list_keys)
    data.f1.close()

    new_dict = data.segmentation()
    lk = list(data.data.keys())
    for i in lk:
        data.SegmentalSearch(i, new_dict)
    data.f2.close()

if __name__ == "__main__":
    main()