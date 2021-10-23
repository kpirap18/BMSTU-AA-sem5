using System.Threading;

namespace Enumeration_sort
{
    static class EnumeSort
    {
        public static int[] b;//результирующая последовательность
        public static string Sequential(ref int[] a)
        {
            int n = a.Length;
            int[] b = new int[n];
            int x;
            string str = "";
            // по всем элементам
            for (int i = 0; i < n; i++)
            {
                x = 0;
                // вычисляем ранг элемента
                for (int j = 0; j < n; j++)
                    if (a[i] > a[j] || (a[i] == a[j] && j > i))
                        x++;
                b[x] = a[i]; // записываем в результирующую
            }
            //запись в строку элементов массива
            foreach (var item in b)
                str += item + " ";
            return str;
        }

        public static string Parallel(int[] a)
        {
            int M = 1;//основываясь на предыдущих работах, берем оптимальное число потоков
            Thread[] thrs = new Thread[M];
            int[] b = new int[n];
            int n = a.Length;
            string str = "";
            //инициализируем каждый поток в массиве
            for (int i = 0; i < M; i++)
            {
                //локальный индекс. иначе i-ссылка. когда поток начнет работу, i убежит далеко
                int thr = i;
                thrs[i] = new Thread(() =>
                {
                    for (int j = thr; j < n; j += M)//даем потоку обработать определенные элементы(примерно равные порции)
                    {
                        int x = 0;
                        // вычисляем ранг элемента
                        for (int k = 0; k < n; k += M)
                            if (a[j] > a[k] || (a[j] == a[k] && k > j))
                                x++;
                        b[x] = a[j]; // записываем в результирующую
                    }
                });
                //запускаем потоки
                thrs[i].Start();
            }

            //останавливаем потоки
            for (int i = 0; i < M; i++) thrs[i].Join();
            //запись в строку элементов массива
            foreach (var item in b)
                str += item + " ";
            return str;
        }
    }
}