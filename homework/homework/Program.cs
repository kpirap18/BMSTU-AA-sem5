using System;

namespace homework
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            int size_ = 6;                                  // (1)
            int[] arr = new int[size_];                     // (2)

            int left = 0;                                   // (3)
            int right = size_ - 1;                          // (4)

            for (int i = 0; i < size_; i++)                 // (5)
            {
                arr[i] = size_ - i;                         // (6)
            }

            for (int i = 0; i < size_; i++)                 
            {
                Console.Write(arr[i]);
            }
            Console.WriteLine();

            while (left <= right)                           // (7)
            {
                for (int i = left; i < right; i++)          // (8)
                {
                    if (arr[i] > arr[i + 1])                // (9)
                    {
                        int buf = arr[i];                   // (10)
                        arr[i] = arr[i + 1];                // (11)
                        arr[i + 1] = buf;                   // (12)
                    }
                }
                right--;                                    // (13)

                for (int i = right - 1; i > left - 1; i--)  // (14)
                {   
                    if (arr[i] > arr[i + 1])                // (15)
                    {
                        int buf = arr[i];                   // (16)
                        arr[i] = arr[i + 1];                // (17)
                        arr[i + 1] = buf;                   // (18)
                    }
                }
                left++;                                     // (19)
            }

            for (int i = 0; i < size_; i++)
            {
                Console.Write(arr[i]);
            }
        }
    }
}
