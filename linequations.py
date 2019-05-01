#!/usr/bin/env python3
""" Create system of linear equations. """

import random

MIN_K = -5
MAX_K = 5

def create_system(num_eq, num_var):
    """ Create random system of linear equations. """
    random.seed()

    variables = [0] * num_var
    for i in range(num_var):
        variables[i] = random.randrange(MIN_K, MAX_K)

    coefficients = [[0] * num_var for _ in range(num_eq)]
    constants = [0] * num_eq

    for i in range(num_eq):
        for j in range(num_var):
            coefficients[i][j] = random.randrange(MIN_K, MAX_K)
            constants[i] += coefficients[i][j]*variables[j]

    for i in range(num_eq):
        for j in range(num_var):
            print(" {: } ".format(coefficients[i][j]), end='')
        print("| {: }".format(constants[i]))

    return (coefficients, constants, variables)

def main():
    """ Main. """
    num_eq = int(input("Number of equations: "))
    num_var = int(input("Number of variables: "))
    create_system(num_eq, num_var)

if __name__ == '__main__':
    main()
