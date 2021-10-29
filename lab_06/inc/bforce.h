#ifndef BFORCE_H
#define BFORCE_H

#include "define.h"
#include "matrix.h"
#include "city.h"
#include "array.h"

void get_routes(sarray *cities, sarray *res_,
                sarray result[MAXRECURSION],
                int matrix[N][N], int *len);

sarray get_shortest_path(sarray cities, int matrix[N][N]);

int get_path_cost(sarray cities, int matrix[N][N]);

#endif // BFORCE_H
