import numpy as np
import pandas as pd
import euler_sol
import rk_sol
import splines
import math

file_V_int = "V_coef.txt"
file_m_int = "m_coef.txt"
file_n_int = "n_coef.txt"
file_h_int = "h_coef.txt"

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
    runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    df = pd.DataFrame(runge_kutta_sol)
    df.to_csv('out_rk.csv')

    # Runge-Kutta Solution for different values of n
    # n = 10000
    # runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    # df = pd.DataFrame(runge_kutta_sol)
    # df.to_csv('out_rk_10000.csv')

    # n = 50000
    # runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    # df = pd.DataFrame(runge_kutta_sol)
    # df.to_csv('out_rk_50000.csv')

    # Cubic Splines Interpolation
    coef = splines.splines(runge_kutta_sol)
    coef_V, coef_m, coef_n, coef_h = coef[0], coef[1], coef[2], coef[3]
    print_coef(coef_V, file_V_int)
    print_coef(coef_m, file_m_int)
    print_coef(coef_n, file_n_int)
    print_coef(coef_h, file_h_int)

    #Convergence Table
    # m = 8

    # with open("behavior_convergence_rk.txt", 'w', encoding='utf-8') as file2:
    #     file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n")
    #     e=q=r=0
    #     h = [0]*m
    #     yn = [y_0]*m

    #     for i in range(1, m + 1):
    #         n = 1000*2**(i-1)
    #         h[i-1] = (T[1] - T[0])/n
    #         yn[i-1] = rk_sol.rk_solution(T, n, y_0, constants)
    #         if i > 2:
    #             q = abs((yn[i-3][-1][1]-yn[i-2][-1][1])/(yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             r = h[i-2]/h[i-1]
    #             p = math.log(q)/math.log(r)
    #             e = abs((yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(n,h[i-1],e,p))
    
    return

main()
