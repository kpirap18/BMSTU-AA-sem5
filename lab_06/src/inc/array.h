#ifndef ARRAY_H
#define ARRAY_H

#include "define.h"

typedef struct
{
    int len;
    int array[N + 2];
} sarray;

void print_array(sarray cities, char msg[1000]);

void add_element(sarray *cities, const int element);

int get_element(sarray arr, int const index);

int del_element(sarray *cities, int index);

sarray copy_array(sarray arr);

#endif // ARRAY_H
