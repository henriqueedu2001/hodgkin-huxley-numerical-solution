import numpy as np
from scipy.optimize import fsolve
import numpy as np
import pandas as pd
import eq_parameters
import state_variables
import cauchy_function

def ie_sol(time_interval: (float, float), n_steps: int, initial_y: np.array, constants: dict):
    discretize_domain, delta_t = cauchy_function.discretize_interval(time_interval, n_steps)
    
    solution = []
    
    y_aprox = [initial_y]  
    
    for k in range(1, len(discretize_domain)):
        y_prev = y_aprox[-1]  
        t_k = discretize_domain[k]

        def equation(y_next):
            return y_prev + delta_t * cauchy_function.cauchy_function(t_k, y_next, constants) - y_next       

        y_k_plus_1 = fsolve(equation, y_prev + delta_t * cauchy_function.cauchy_function(t_k, y_prev, constants))
        
        y_aprox.append(y_k_plus_1)
 
    for k, y_k in enumerate(y_aprox):
        t_k = np.array([discretize_domain[k]])
        time_stamped_sol = np.concatenate((t_k, y_k))
        solution.append(time_stamped_sol)
        
    return solution



