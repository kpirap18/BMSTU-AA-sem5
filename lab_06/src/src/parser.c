#include <stdio.h>
#include <string.h>

#include "parser.h"
#include "matrix.h"
#include "city.h"

int parser(FILE *f, char cities[N], int matrix[N][N])
{
    char fcity;
    char scity;

    int cost, len = 0;

    int i, j;

    char s[100];
    char s2[] = "--";

    while (!strstr(s, s2))
        fscanf(f, "%s", s);
    fseek(f, -4, SEEK_CUR);

    while (!feof(f))
    {
        fscanf(f, "    %c -- %c [label=\"%d\"];", &fcity, &scity, &cost);

        if ((fcity == '}') || (scity == '}'))
            break;

        i = find_city(cities, fcity, &len);
        j = find_city(cities, scity, &len);

        matrix[i][j] = cost;
        matrix[j][i] = cost;
    }

    return len;
}

int parser_to_dot(char fname[20], char cities[N], int matrix[N][N], 
                  sarray result, int len, char color[10])
{
    FILE *f = fopen(fname, "w");
    char first, second; 

    if (!f)
    {
        printf("Ошибка открытия файла\n");
        return ERROPENFILE;
    }

    fputs(DOT_BEGIN, f);

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < i; j++)
        {
            first = cities[j];
            second = cities[i];

            int flag = 0;

            for (int k = 0; k < result.len - 1; k++)
            {
                if ((i == result.array[k]) && 
                    (j == result.array[k + 1]) ||
                    (j == result.array[k]) && 
                    (i == result.array[k + 1]))
                    {
                        flag = 1;
                    }
            }

            if (flag)
                fprintf(f, "    %d -- %d [label=\"%d\", color=%s, penwidth=2.0];\n", 
                        i, j, matrix[i][j], color);
            else
                fprintf(f, "    %d -- %d [label=\"%d\"];\n", i, j, matrix[i][j]);

            flag = 0;

            
        }
    }

    fputs(DOT_END, f);

    fclose(f);

    return OK;
}
