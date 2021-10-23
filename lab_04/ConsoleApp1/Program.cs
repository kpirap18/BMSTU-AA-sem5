using System;
using System.IO;
using System.Linq;

namespace Enumeration_sort
{
    class Program
    {
        //заполнение случайными числами от 0 до кол-ва элементов
        static void GenerateRandArray(int n)
        {
            Random Rand = new Random();
            using (StreamWriter file = new StreamWriter("C:\\Users\\kiv09\\Documents\\lll\\in.txt", true))
            {
                for (int i = 0; i < n; i++)
                    file.Write(Rand.Next(0, n) + " ");
                file.Write(Environment.NewLine);
            }
        }
        //заполнение числами от 0 до n по возрастанию
        static void GenerateAscArray(int n)
        {
            using (StreamWriter file = new StreamWriter("C:\\Users\\kiv09\\Documents\\lll\\in.txt", true))
            {
                for (int i = 0; i < n; i++)
                    file.Write(i + " ");
                file.Write(Environment.NewLine);
            }
        }
        //заполнение числами от 0 до n по убыванию
        static void GenerateDescArray(int n)
        {
            using (StreamWriter file = new StreamWriter("C:\\Users\\kiv09\\Documents\\lll\\in.txt", true))
            {
                for (int i = n - 1; i >= 0; i--)
                    file.Write(i + " ");
                file.Write(Environment.NewLine);
            }
        }
        static void Main(string[] args)
        {
            //неупорядоченный набор данных
            GenerateRandArray(100);
            GenerateRandArray(1000);
            GenerateRandArray(10000);
            GenerateRandArray(50000);
            GenerateRandArray(80000);
            GenerateRandArray(100000);
            //упорядоченный набор данных по возрастанию
            GenerateAscArray(100);
            GenerateAscArray(1000);
            GenerateAscArray(10000);
            GenerateAscArray(50000);
            GenerateAscArray(80000);
            GenerateAscArray(100000);
            //упорядоченный набор данных по убыванию
            GenerateDescArray(100);
            GenerateDescArray(1000);
            GenerateDescArray(10000);
            GenerateDescArray(50000);
            GenerateDescArray(80000);
            GenerateDescArray(100000);

            string str = "";

            //чтение из файла. Каждую строчку преобразуем массив, применяем последовательную и параллельную сортировку.
            using (StreamReader file = new StreamReader("C:\\Users\\kiv09\\Documents\\lll\\in.txt"))
            {
                string line;
                DateTime d1, d2;
                while ((line = file.ReadLine()) != null)
                {
                    //получаем массив из файла
                    int[] a = line.Split(new char[] { ' ', }, StringSplitOptions.RemoveEmptyEntries).Select(n => int.Parse(n)).ToArray();
                    //последовательная сортировка 
                    d1 = DateTime.Now;
                    str = EnumeSort.Sequential(ref a);
                    d2 = DateTime.Now;
                    Console.WriteLine("Seq Complete");
                    //сразу записываем в файл строку - остортированный по рангам исходный массив
                    File.AppendAllText("C:\\Users\\kiv09\\Documents\\lll\\out.txt",
                        str + Environment.NewLine);
                    File.AppendAllText("C:\\Users\\kiv09\\Documents\\lll\\sum1.txt",
                        (d2 - d1).TotalMilliseconds +  " милисекундыб прост" + Environment.NewLine);
                    //перед использованием статического элемента нужно обнуление
                    EnumeSort.b = null;
                    EnumeSort.b = new int[a.Length];//переопределяем элемент
                    d1 = DateTime.Now;
                    str = EnumeSort.Parallel(a);
                    d2 = DateTime.Now;
                    Console.WriteLine("Par Complete");
                    //сразу записываем в файл строку - остортированный по рангам исходный массив
                    File.AppendAllText("C:\\Users\\kiv09\\Documents\\lll\\out.txt",
                        str + Environment.NewLine);
                    File.AppendAllText("C:\\Users\\kiv09\\Documents\\lll\\sum1.txt",
                        (d2 - d1).TotalMilliseconds + " милисекундыб расп" + Environment.NewLine);
                }
            }
            Console.WriteLine("Done!");
            Console.ReadKey();
        }
    }
}