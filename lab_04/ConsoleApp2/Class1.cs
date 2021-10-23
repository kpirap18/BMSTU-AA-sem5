using System.Collections.Concurrent;
using System.Threading.Tasks;

namespace Lab4Csh
{
    static class Utils
    {
        //заполнение числами от 0 до n по возрастанию
        public static int[] GenerArray(int n)
        {
            var a = new int[n];
            for (int i = 0; i < n; i++)
                a[n - i - 1] = i;
            return a;
        }

        public static int[] SortSeq(this int[] a)
        {
            int n = a.Length;
            int[] b = new int[n];
            int x;
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
            return b;
        }

        public static int[] SortParall(this int[] a)
        {
            int n = a.Length;
            int[] b = new int[n];
            Parallel.ForEach(Partitioner.Create(0, n), range =>
            {
                int x;
                for (int i = range.Item1; i < range.Item2; i++)
                {
                    x = 0;
                    // вычисляем ранг элемента
                    for (int j = 0; j < n; j++)
                        if (a[i] > a[j] || (a[i] == a[j] && j > i))
                            x++;
                    b[x] = a[i]; // записываем в результирующую
                }
            }
            );
            return b;
        }
    }
}