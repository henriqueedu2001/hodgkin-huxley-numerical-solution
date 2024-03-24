import numpy as np
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

def splines(solution: list):
    t, V, m, n, h = zip(*solution)

    sorted_indices = np.argsort(t)
    t_sorted = np.array(t)[sorted_indices]
    V_sorted = np.array(V)[sorted_indices]
    m_sorted = np.array(m)[sorted_indices]
    n_sorted = np.array(n)[sorted_indices]
    h_sorted = np.array(h)[sorted_indices]

    V_int = CubicSpline(t_sorted, V_sorted, bc_type='natural')
    m_int = CubicSpline(t_sorted, m_sorted, bc_type='natural')
    n_int = CubicSpline(t_sorted, n_sorted, bc_type='natural')
    h_int = CubicSpline(t_sorted, h_sorted, bc_type='natural')

    V_coef = V_int.c
    m_coef = m_int.c
    n_coef = n_int.c
    h_coef = h_int.c

    points_V = np.array(list(zip(t_sorted, V_int(t_sorted))))
    points_m = np.array(list(zip(t_sorted, m_int(t_sorted))))
    points_n = np.array(list(zip(t_sorted, n_int(t_sorted))))
    points_h = np.array(list(zip(t_sorted, h_int(t_sorted))))

    return V_coef, m_coef, n_coef, h_coef, points_V, points_m, points_n, points_h    
    
