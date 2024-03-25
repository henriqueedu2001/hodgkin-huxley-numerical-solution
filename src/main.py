import numpy as np
import pandas as pd
import implicit_euler
import euler_sol
import rk_sol
import splines
import math

def print_coef(coef, file):
    with open(file, 'w') as file:
        file.write("a_i & b_i & c_i & d_i \\\\ \n")
        for i in range(0, len(coef), 4):
            line = ' & '.join(["{:.4f}".format(value) for value in coef[i:i+4]]) + ' \\\\ \n'
            file.write(line)

def main():
    constants = {
        'current': 0., 
        'capacitance': 1.,
        'g_Na': 120.,
        'g_K': 36., 
        'g_L': 0.3,
        'E_Na': 115., 
        'E_K':  -12.0, 
        'E_L':  10.613
    }
    
    T = [0, 30]
    n = 5000
    
    y_0 = np.array([
            0., # V
            0.05,  # m
            0.6,  # h
            0.06  # n
        ])
    
    #print(cauchy_function(0, y_0, constants))
    
    # e_sol = euler_sol.euler_solution(T, n, y_0, constants)
    # df = pd.DataFrame(e_sol)
    # df.to_csv('out_euler.csv')    

    # Runge-Kutta Solution
    
    # n_values = [30, 100, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000]
    n_values = [30, 50, 100, 200, 300, 500, 
            1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 90000,
            10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
            ]
    
    for n in n_values:
        print(f'n = {n}')
        implicit_euler_sol = implicit_euler.implicit_euler_solution(T, n, y_0, constants)
        df = pd.DataFrame(implicit_euler_sol)
        df.to_csv(f'imgs/implicit_euler_out/out_imp_euler_{n}.csv')
    
    for n in n_values:
        print(f'n = {n}')
        RK = rk_sol.rk_solution(T, n, y_0, constants)
        df = pd.DataFrame(RK)
        df.to_csv(f'imgs/rk_out/out_rk_{n}.csv')

    # # Get the coefficients of the interpolation
    # print_coef(coef_V, file_V_int)
    # print_coef(coef_m, file_m_int)
    # print_coef(coef_n, file_n_int)
    # print_coef(coef_h, file_h_int)

    # # Get the points from the interpolation
    # df = pd.DataFrame(points_V)
    # df.to_csv('interpolated_points_V.csv')    
    # df = pd.DataFrame(points_m)
    # df.to_csv('interpolated_points_m.csv')  
    # df = pd.DataFrame(points_n)
    # df.to_csv('interpolated_points_n.csv')  
    # df = pd.DataFrame(points_h)
    # df.to_csv('interpolated_points_h.csv')    

    return

main()
