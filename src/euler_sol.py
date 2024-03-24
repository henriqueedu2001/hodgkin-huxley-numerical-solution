import numpy as np
import pandas as pd
import eq_parameters
import state_variables
import cauchy_function

def euler_solution(time_interval: (float, float), n_steps: int, initial_y: np.array, constants: dict):
    """Computes a numerical solution for the y(t) = [V(t), m(t), h(t), n(t)], the solution of the
    Hodgkin-Huxley differential equation via Euler's method: y_{k+1} = y_k + f(t_k, y_k)*delta_t

    Args:
        time_interval ((float, float)): domain of the function (interval [a,b]) 
        n_steps (int): number of steps for discretize the domain
        initial_y (np.array): the initial value of the vector y: y(0) = [V(0), m(0), h(0), n(0)]
        constants: the constants g_Na, g_K, g_L, E_Na, E_K and E_L of the model
        
    Returns:
        (np.array, np.array): tupla (X, Y), em que X = [t_0, t_1, t_2, ..., t_{n-1}] é 
        o domínio discretizado e Y = [y_0, y_1, y_2, ..., y_{n-1}] é a solução aproximada
        pelo método de euler(y_{k+1} = y_k + f(t_k, y_k)*delta_t)
    """
    
    discretize_domain, delta_t = cauchy_function.discretize_interval(time_interval, n_steps)
    
    solution = []
    
    y_aprox = []
    
    # y_0 = y(0)
    y_aprox.append(initial_y)
    
    # evaluates y_{k+1} with y_k and t_k
    for k, t_k in enumerate(discretize_domain[:-1]):
        y_k = y_aprox[k]
        
        #Explicit Euler
        next_y = y_k + cauchy_function.cauchy_function(t_k, y_k, constants)*delta_t
        y_aprox.append(next_y)
    
    # adds time stamps
    for k, y_k in enumerate(y_aprox):
        t_k = np.array([discretize_domain[k]])
        time_stamped_sol = np.concatenate((t_k, y_k))
        solution.append(time_stamped_sol)
        
    # solution = np.array(solution)
    
    return solution
