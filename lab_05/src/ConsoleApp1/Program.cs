using System;
using System.IO;
using System.Threading;
using System.Collections.Generic;

using intPtr = System.Collections.Generic.List<int>;
using longPtr = System.Collections.Generic.List<long>;

namespace Lab5
{
    class Program
    {
        static longPtr time1in = new longPtr();
        static longPtr time1out = new longPtr();
        static longPtr time2in = new longPtr();
        static longPtr time2out = new longPtr();
        static longPtr time3in = new longPtr();
        static longPtr time3out = new longPtr();
        static longPtr time4in = new longPtr();

        static object FStage = new object();
        static object SStage = new object();
        static object TStage = new object();

        public const double CountOfOperations = 5000;

        public static intPtr CreateRandArray(int n)
        {
            intPtr array = new intPtr();

            var random = new Random();

            for (int i = 0; i < n; i++)
            {
                array.Add(random.Next(1, 1000));
            }

            PrintArray2(array);
            return array;
        }

        public static Queue<intPtr> CreateQueue(int lenQueue, int countElem)
        {
            Queue<intPtr> queue = new Queue<intPtr>();

            for (int i = 0; i < lenQueue; i++)
            {
                Int64 t = DateTime.Now.Ticks;
                time1in.Add(t);
                Console.Write("{0}: ", i + 1);
                queue.Enqueue(CreateRandArray(countElem));
            }

            return queue;
        }

        public static void PrintArray(longPtr array)
        {
            foreach (var elem in array)
            {
                //DateTime d = new DateTime(elem);
                Console.Write("{0}, ", elem);

            }
            Console.WriteLine();
        }

        public static void PrintArray2(intPtr array)
        {
            foreach (var elem in array)
            {
                //DateTime d = new DateTime(elem);
                Console.Write("{0}, ", elem);

            }
            Console.WriteLine();
        }

        public static void PrintQueue(Queue<longPtr> queue)
        {
            if (queue.Count == 0)
            {
                Console.WriteLine("Queue is empty.\n");
                return;
            }

            foreach (var elem in queue)
            {
                PrintArray(elem);
            }

            Console.WriteLine();
        }

        public static int AvgArrayInt(intPtr array)
        {
            int avg_int = 0;
            int count = 0;

            for (int i = 0; i < CountOfOperations; i++)
            {
                avg_int = 0;
                count = 0;
                foreach (var el in array)
                {
                    avg_int += el;
                    count++;
                }
            }

            avg_int /= count;

            return avg_int;
        }

        public static int CountBigAvgInt(intPtr array, int num)
        {
            int count = 0;

            for (int i = 0; i < CountOfOperations; i++)
            {
                count = 0;
                foreach (var el in array)
                {
                    if (el > num)
                    {
                        count++;
                    }
                }
            }

            return count;
        }

        public static int CountIsProc(int num)
        {
            int res = 1;
            for (int k = 0; k < CountOfOperations; k++)
            {
                if (num > 1)
                {
                    for (int i = 2; i < num; i++)
                    {
                        if (num % i == 0)
                        {
                            res = 0;
                            break;
                        }
                    }
                }
                else
                {
                    res = 0;
                }
            }

            return res;
        }

        public static void Conveyor(object obj)
        { 
            ThreadArgs args = (ThreadArgs)obj;
            int avg = 0, count = 0, proc = 0;
            
            intPtr array;

            if (args.firstQueue.Count != 0)
            { 
                lock (args.firstQueue)
                {
                    Int64 t = DateTime.Now.Ticks;
                    time1out.Add(t);
                    array = args.firstQueue.Dequeue();
                }

                lock (FStage)
                {
                    Int64 t1, t2;
                    t1 = DateTime.Now.Ticks;
                    Console.WriteLine("Лента 1 \t{0} \t1 \t{1}",
                        Thread.CurrentThread.Name,
                        t1);

                    avg = AvgArrayInt(array);

                    t2 = DateTime.Now.Ticks;
                    Console.WriteLine("Лента 1 \t{0} \t0 \t{1} \t{2}",
                        Thread.CurrentThread.Name,
                        t1, t2 - t1);
                    Console.WriteLine("Результат: {0}", avg);
                }

                lock (args.secondQueue)
                {
                    Int64 t = DateTime.Now.Ticks;
                    time2in.Add(t);
                    args.secondQueue.Enqueue(array);
                }
            }


            if (args.secondQueue.Count != 0)
            {
                lock (SStage)
                {
                    Int64 t1, t2;
                    t1 = DateTime.Now.Ticks;
                    Console.WriteLine("Лента 2 \t{0} \t1 \t{1}",
                        Thread.CurrentThread.Name,
                        t1);

                    lock (args.secondQueue)
                    {
                        Int64 t = DateTime.Now.Ticks;
                        time2out.Add(t);
                        array = args.secondQueue.Dequeue();
                    }

                    count = CountBigAvgInt(array, avg);

                    t2 = DateTime.Now.Ticks;
                    Console.WriteLine("Лента 2 \t{0} \t0 \t{1} \t{2}",
                        Thread.CurrentThread.Name,
                        t1, t2 - t1);
                    Console.WriteLine("Результат: {0}", count);
                }

                lock (args.thirdQueue)
                {
                    Int64 t = DateTime.Now.Ticks;
                    time3in.Add(t);
                    args.thirdQueue.Enqueue(array);
                }
            }


            if (args.thirdQueue.Count != 0)
            {
                lock (TStage)
                {
                    Int64 t1, t2;
                    t1 = DateTime.Now.Ticks;
                    Console.WriteLine("Лента 3 \t{0} \t1 \t{1}",
                        Thread.CurrentThread.Name,
                        t1);

                    lock (args.thirdQueue)
                    {
                        Int64 t = DateTime.Now.Ticks;
                        time3out.Add(t);
                        array = args.thirdQueue.Dequeue();
                    }

                    proc = CountIsProc(count);


                    t2 = DateTime.Now.Ticks;
                    time4in.Add(t2);
                    Console.WriteLine("Лента 3 \t{0} \t0 \t{1} \t{2}",
                        Thread.CurrentThread.Name,
                        t1, t2 - t1);
                    Console.WriteLine("Результат: {0}", proc);
                }
            }
        }

        public static void MainTread(Queue<intPtr> queue)
        {
            Int64 t1, t2, t11, t22;

            t1 = DateTime.Now.Ticks;
            int avg, count, proc;

            foreach (var el in queue)
            {
                t11 = DateTime.Now.Ticks;
                avg = AvgArrayInt(el);
                t22 = DateTime.Now.Ticks;
                Console.WriteLine("Оператор 1 \t{0} \t{1}",
                        t11, t22 - t11);

                t11 = DateTime.Now.Ticks;
                count = CountBigAvgInt(el, avg);
                t22 = DateTime.Now.Ticks;
                Console.WriteLine("Оператор 2 \t{0} \t{1}",
                        t11, t22 - t11);

                t11 = DateTime.Now.Ticks;
                proc = CountIsProc(count);
                t22 = DateTime.Now.Ticks;
                Console.WriteLine("Оператор 3 \t{0} \t{1}",
                        t11, t22 - t11);
            }

            t2 = DateTime.Now.Ticks;

            Console.WriteLine("Простая реализация: {0}\n", t2 - t1);

            Console.WriteLine("\n\nProcess:\n");

            t1 = DateTime.Now.Ticks;

            ThreadArgs args = new ThreadArgs(queue);

            Thread FThread = new Thread(new ParameterizedThreadStart(Conveyor));
            FThread.Name = "Поток 1";

            Thread SThread = new Thread(new ParameterizedThreadStart(Conveyor));
            SThread.Name = "Поток 2";

            Thread TThread = new Thread(new ParameterizedThreadStart(Conveyor));
            TThread.Name = "Поток 3";

            FThread.Start(args);
            SThread.Start(args);
            TThread.Start(args);

            while (args.firstQueue.Count != 0)
            {
                if (!FThread.IsAlive)
                {
                    FThread = new Thread(new ParameterizedThreadStart(Conveyor));
                    FThread.Name = "Поток 1";
                    FThread.Start(args);
                }

                if (!SThread.IsAlive)
                {
                    SThread = new Thread(new ParameterizedThreadStart(Conveyor));
                    SThread.Name = "Поток 2";
                    SThread.Start(args);
                }

                if (!TThread.IsAlive)
                {
                    TThread = new Thread(new ParameterizedThreadStart(Conveyor));
                    TThread.Name = "Поток 3";
                    TThread.Start(args);
                }
            }

            FThread.Join();
            SThread.Join();
            TThread.Join();

            t2 = DateTime.Now.Ticks;

            Console.WriteLine("Конвейер: {0}\n", t2 - t1);
        }


        static void Main(string[] args)
        {
            Console.WriteLine("{0}", DateTime.Now);
            int count, len_;
            Console.WriteLine("Input count of arrays: ");
            if (!(int.TryParse(Console.ReadLine(), out count)))
            {
                Console.WriteLine("Ошибка");
                Environment.Exit(0);
            }

            Console.WriteLine("Input len of arrays: ");
            if (!(int.TryParse(Console.ReadLine(), out len_)))
            {
                Console.WriteLine("Ошибка");
                Environment.Exit(0);
            }

            Console.WriteLine("\n\nМассивы по задачам: ");
            Queue<intPtr> queue = CreateQueue(count, len_);
            Console.WriteLine("\n\n");
            MainTread(queue);

            PrintArray(time1in);
            PrintArray(time1out);
            PrintArray(time2in);
            PrintArray(time2out);
            PrintArray(time3in);
            PrintArray(time3out);
            PrintArray(time4in);
        }
    }

    public class ThreadArgs
    {
        public Queue<intPtr> firstQueue = null;
        public Queue<intPtr> secondQueue = new Queue<intPtr>();
        public Queue<intPtr> thirdQueue = new Queue<intPtr>();

        public List<Int64> t1, t2, t3, t4, t5, t6;

        public ThreadArgs(Queue<intPtr> queue)
        {
            firstQueue = queue;

            t1 = new List<Int64>();
            t2 = new List<Int64>();
            t3 = new List<Int64>();
            t4 = new List<Int64>();
            t5 = new List<Int64>();
            t6 = new List<Int64>();
        }
    }
}


// len = [10, 25, 50, 500, 10000, 50000, 100000, 500000]
// simple = [34783, 64132, 177235, 733111, 23997915, 138152405, 238140692, 1368964823] 
// con = [566716, 589083, 908572, 1444050, 23651996, 137199030, 211956092, 1195390050]