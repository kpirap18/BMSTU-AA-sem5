#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>

#include "define.h"
#include "bforce.h"
#include "matrix.h"
#include "city.h"
#include "array.h"
#include "antalgorithm.h"
#include "parser.h"

int64_t tick(void)
{
    uint32_t high, low;
    __asm__ __volatile__(
        "rdtsc\n"
        "movl %%edx, %0\n"
        "movl %%eax, %1\n"
        : "=r"(high), "=r"(low)::"%rax", "%rbx", "%rcx", "%rdx");

    uint64_t ticks = ((uint64_t)high << 32) | low;

    return ticks;
}

int main(int argc, char *argv[])
{
    float alpha[9] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};
    float p[9] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};
    int tmax[9] = {100, 150, 200, 250, 300, 350, 400, 450, 500};

    srand(time(NULL));
    int min_ant;
    int matrix[N][N];
    char city_names[N];
    sarray cities;
    sarray result;
    int len;

    if (argv[1][0] == '1')
    {
        int min_ant2;
        int min_ant3;
        
        // ###### 1 МАТРИЦА ###### //
        char fname[20] = "graph.dot";

        FILE *f = fopen(fname, "r");
        if (!f)
        {
            printf("Ошибка открытия файла\n");
            return ERROPENFILE;
        }
        len = parser(f, city_names, matrix);
        fclose(f);

        create_cities_array(&cities, len);

        // print_cities(cities, city_names);
        sarray copy_cities = copy_array(cities);
        print_matrix(matrix, len);

        result = get_shortest_path(&copy_cities, matrix);
        int min_simple = get_cost(result, matrix);

        print_array(result, "result!!!!!!!!!!!!!!!!");
        // ###### 1 МАТРИЦА ###### //

        // ###### 2 МАТРИЦА ###### //
        int matrix2[N][N];
        char city_names2[N];
        sarray cities2;
        char fname2[20] = "graph1.dot";

        FILE *f2 = fopen(fname2, "r");
        if (!f)
        {
            printf("Ошибка открытия файла\n");
            return ERROPENFILE;
        }
        int len2 = parser(f2, city_names2, matrix2);
        fclose(f2);

        create_cities_array(&cities2, len2);

        // print_cities(cities2, city_names2);
        sarray copy_cities2 = copy_array(cities2);
        print_matrix(matrix2, len2);

        sarray result2 = get_shortest_path(&copy_cities2, matrix2);
        int min_simple2 = get_cost(result2, matrix2);

        print_array(result2, "result!!!!!!!!!!!!!!!!");
        // ###### 2 МАТРИЦА ###### //

        // ###### 3 МАТРИЦА ###### //
        int matrix3[N][N];
        char city_names3[N];
        sarray cities3;
        char fname3[20] = "graph2.dot";

        FILE *f3 = fopen(fname3, "r");
        if (!f)
        {
            printf("Ошибка открытия файла\n");
            return ERROPENFILE;
        }
        int len3 = parser(f3, city_names3, matrix3);
        fclose(f3);

        create_cities_array(&cities3, len3);

        // print_cities(cities3, city_names3);
        sarray copy_cities3 = copy_array(cities3);
        print_matrix(matrix3, len3);

        sarray result3 = get_shortest_path(&copy_cities3, matrix3);
        int min_simple3 = get_cost(result3, matrix3);

        print_array(result3, "result!!!!!!!!!!!!!!!!");
        // ###### 3 МАТРИЦА ###### //

        // ###### LOG  FILE ###### //
        FILE *fout = fopen("result.txt", "w");
        for (int i = 0; i < 9; i++)
        {
            for (int k = 0; k < 9; k++)
            {
                for (int j = 0; j < 9; j++)
                {
                    sarray res_ant = ant_alg(matrix, len,
                                            cities, tmax[j],
                                            alpha[i],
                                            1 - alpha[i], p[k]);
                    min_ant = get_cost(res_ant, matrix);

                    sarray res_ant2 = ant_alg(matrix2, len,
                                            cities2, tmax[j],
                                            alpha[i],
                                            1 - alpha[i], p[k]);
                    min_ant2 = get_cost(res_ant2, matrix2);

                    sarray res_ant3 = ant_alg(matrix3, len,
                                            cities3, tmax[j],
                                            alpha[i],
                                            1 - alpha[i], p[k]);
                    min_ant3 = get_cost(res_ant3, matrix3);


                    fprintf(fout, "%.1f &%.1f &%d &%d &%d &%d\n",
                            p[k], alpha[i], 
                            tmax[j], abs(min_simple - min_ant), 
                            abs(min_simple2 - min_ant2), 
                            abs(min_simple3 - min_ant3));

                }
            }
        }
        fclose(fout);
        // ###### LOG  FILE ###### //
    }
    else
    {
        char fname_test[20];
        sarray res_ant;

        printf("Название файла: ");
        scanf("%s", fname_test);

        FILE *f = fopen(fname_test, "r");
        if (!f)
        {
            printf("Ошибка открытия файла\n");
            return ERROPENFILE;
        }
        int len = parser(f, city_names, matrix);
        fclose(f);

        create_cities_array(&cities, len);

        sarray copy_cities = copy_array(cities);
        print_matrix(matrix, len);

        FILE *fout = fopen("res_test.txt", "w");
        int64_t time_s = tick();
        sarray result = get_shortest_path(&copy_cities, matrix);
        int min_simple = get_cost(result, matrix);
        int64_t time_e = tick();

        // вывод инфы про полный перебор 
        print_array(result, "Результат полного перебора");
        printf("Минимальный путь = %d\n", min_simple);
        printf("Время выполнения %d\n\n", time_e - time_s);

        int count = 0;
        time_s = tick();
        
        for (int i = 0; i < 9; i++)
        {
            for (int k = 0; k < 9; k++)
            {
                for (int j = 0; j < 9; j++)
                {
                    count++;
                    res_ant = ant_alg(matrix, len,
                                            cities, tmax[j],
                                            alpha[i],
                                            1 - alpha[i], p[k]);
                    min_ant = get_cost(res_ant, matrix);

                    fprintf(fout, "%.1f, %.1f, %d, %d\n",
                            p[k], alpha[i], 
                            tmax[j], abs(min_simple - min_ant));

                }
            }
        }
        fclose(fout);
        time_e = tick();

        // вывод инфы про мур перебор последний вариант
        print_array(res_ant, "Результат муравьиного алгоритма (последняя итерация)");
        printf("Минимальный путь = %d\n", min_ant);
        printf("Время выполнения %f\n", (float)(time_e - time_s) / (float)count);

        parser_to_dot("res_test_sim.dot", city_names, matrix, result, len, "green");
        system("sfdp -Tpng res_test_sim.dot -o res_test_sim.png");
        system("xdg-open res_test_sim.png");

        parser_to_dot("res_test_ant.dot", city_names, matrix, result, len, "red");
        system("sfdp -Tpng res_test_ant.dot -o res_test_ant.png");
        system("xdg-open res_test_ant.png");
    }

    
    printf("DONE\n");

    return 0;
}

// "C:/Program Files/Graphviz/bin/dot.exe" -Tpng graph.dot > outway.png
