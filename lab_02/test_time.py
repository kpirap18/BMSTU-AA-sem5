import time
import numpy as np
import random

from main import *


def TimeTest(matrixA, matrixB, countOperations, f):
    t1 = time.process_time()
    for _ in range(countOperations):
        f(matrixA, matrixB)
    t2 = time.process_time()
    return (t2 - t1) / countOperations


def rand_matrix(n):
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(0, 100)

    return a

def prep_test():


    res_stand = []
    res_vin = []
    res_vin_opt = []

    nu = [300]
    for n in nu:
        a = rand_matrix(n)
        b = rand_matrix(n)
        res_stand.append(TimeTest(a, b, 5, simple_matrix_mult))
        res_vin.append(TimeTest(a, b, 5, winograd_matrix_mult))
        res_vin_opt.append(TimeTest(a, b, 5, winograd_matrix_mult_opim))
        print(n)

    res_stand1 = []
    res_vin1 = []
    res_vin_opt1 = []

    for n in nu:
        a = rand_matrix(n + 1)
        b = rand_matrix(n + 1)
        res_stand1.append(TimeTest(a, b, 5, simple_matrix_mult))
        res_vin1.append(TimeTest(a, b, 5, winograd_matrix_mult))
        res_vin_opt1.append(TimeTest(a, b, 5, winograd_matrix_mult_opim))
        print(n)


    print("res_stand", res_stand)
    print()
    print("res_vin", res_vin)
    print()
    print("res_vin_opt", res_vin_opt)


    print("res_stand1", res_stand1)
    print()
    print("res_vin1", res_vin1)
    print()
    print("res_vin_opt1", res_vin_opt1)

prep_test()