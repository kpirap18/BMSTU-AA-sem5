#ifndef ANTALGORITHM_H
#define ANTALGORITHM_H

#include "define.h"
#include "bforce.h"
#include "matrix.h"
#include "ant.h"
#include "array.h"

sarray ant_alg(int matrix[N][N], int len, sarray cities, int tmax,
               float p, float alpha, float beta);

int calc_q(int matrix[N][N], int len);
#endif // ANTALGORITHM_H
