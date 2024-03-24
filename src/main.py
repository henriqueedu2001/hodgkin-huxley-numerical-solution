import numpy as np
import pandas as pd
import euler_sol
import rk_sol
import implicit_euler_sol
import splines
import math

file_V_int = "V_coef.txt"
file_m_int = "m_coef.txt"
file_n_int = "n_coef.txt"
file_h_int = "h_coef.txt"

def print_coef(coef, file):
    with open(file, 'w') as file:
        file.write("a_i & b_i & c_i & d_i \\\\ \n")
        for spline_coef in coef:
            for i in range(0, len(spline_coef), 4):
                line = ' & '.join(["{:.4f}".format(value) for value in spline_coef[i:i+4]]) + ' \\\\ \n'
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
    
    
    # Euler Solution
    # e_sol = euler_sol.euler_solution(T, n, y_0, constants)
    # df = pd.DataFrame(e_sol)
    # df.to_csv('out_euler.csv')    

    # Runge-Kutta Solution
    runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    df = pd.DataFrame(runge_kutta_sol)
    df.to_csv('out_rk.csv')

    # Runge-Kutta Solution for different values of n
    # #n = 5000
    # n = 5000
    # runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    # df = pd.DataFrame(runge_kutta_sol)
    # df.to_csv('out_rk_5000.csv')

    # #n = 10000
    # n = 10000
    # runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    # df = pd.DataFrame(runge_kutta_sol)
    # df.to_csv('out_rk_10000.csv')

    # # n = 50000
    # runge_kutta_sol = rk_sol.rk_solution(T, n, y_0, constants)
    # df = pd.DataFrame(runge_kutta_sol)
    # df.to_csv('out_rk_50000.csv')

    # Implicit Euler Solution
    # imp_euler_sol = implicit_euler_sol.ie_sol(T, n, y_0, constants)
    # df = pd.DataFrame(imp_euler_sol)
    # df.to_csv('out_ie.csv')

    # Implicit Euler Solution for different values of n

    # Cubic Splines Interpolation
    spline = splines.splines(runge_kutta_sol)
    coef_V, coef_m, coef_n, coef_h = spline[0], spline[1], spline[2], spline[3]
    points_V, points_m, points_n, points_h = spline[4], spline[5], spline[6], spline[7]

    print_coef(coef_V, file_V_int)
    print_coef(coef_m, file_m_int)
    print_coef(coef_n, file_n_int)
    print_coef(coef_h, file_h_int)

    df = pd.DataFrame(points_V)
    df.to_csv('interpolated_points_V.csv')    
    df = pd.DataFrame(points_m)
    df.to_csv('interpolated_points_m.csv')  
    df = pd.DataFrame(points_n)
    df.to_csv('interpolated_points_n.csv')  
    df = pd.DataFrame(points_h)
    df.to_csv('interpolated_points_h.csv')    
      
    #Convergence Table for Classic Runge-Kutta
    # m = 10

    # with open("behavior_convergence_rk.txt", 'w', encoding='utf-8') as file2:
    #     file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n")
    #     e=q=r=0
    #     h = [0]*m
    #     yn = [y_0]*m

    #     for i in range(1, m + 1):
    #         n = 500*2**(i-1)
    #         h[i-1] = (T[1] - T[0])/n
    #         yn[i-1] = rk_sol.rk_solution(T, n, y_0, constants)
    #         if i > 2:
    #             q = abs((yn[i-3][-1][1]-yn[i-2][-1][1])/(yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             r = h[i-2]/h[i-1]
    #             p = math.log(q)/math.log(r)
    #             e = abs((yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(n,h[i-1],e,p))

    #Convergence Table for Implicit Euler
    # m = 10

    # with open("behavior_convergence_ie.txt", 'w', encoding='utf-8') as file2:
    #     file2.write("ORDER BEHAVIOR CONVERGENCE TABLE\n")
    #     e=q=r=0
    #     h = [0]*m
    #     yn = [y_0]*m

    #     for i in range(1, m + 1):
    #         n = 500*2**(i-1)
    #         h[i-1] = (T[1] - T[0])/n
    #         yn[i-1] = implicit_euler_sol.ie_sol(T, n, y_0, constants)
    #         if i > 2:
    #             q = abs((yn[i-3][-1][1]-yn[i-2][-1][1])/(yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             r = h[i-2]/h[i-1]
    #             p = math.log(q)/math.log(r)
    #             e = abs((yn[i-2][-1][1]-yn[i-1][-1][1]))
    #             file2.write("{:5d} & {:9.3e} & {:9.3e} & {:9.3e}\\\\\n".format(n,h[i-1],e,p))    
    
    return

main()
