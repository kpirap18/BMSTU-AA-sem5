using System;
using System.Diagnostics;

namespace Lab4Csh
{
    class Program
    {
        static void Main(string[] args)
        {
            Stopwatch st = new Stopwatch();
            Stopwatch st1 = new Stopwatch();

            int[] a;
            int[] b;

            for (int i = 100; i <= 100000; i += 5000)
            {
                a = Utils.GenerArray(i);

                st.Start();
                b = a.SortSeq();
                st.Stop();

                st1.Restart();
                b = a.SortParall();
                st1.Stop();
                Console.WriteLine(string.Format("{0},{1},{2}", i.ToString(), st.ElapsedMilliseconds.ToString(), st1.ElapsedMilliseconds.ToString()));

            }

            Console.WriteLine("Готово!");
            Console.ReadKey();
        }
    }

}