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

def jacobian_hh(V, m, h, n, I, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L):
    """
    Calculate the Jacobian matrix of the Hodgkin-Huxley model.
    
    Args:
        V: Membrane potential.
        m, h, n: State variables.
        I: Applied current.
        C_m: Membrane capacitance.
        g_Na, g_K, g_L: Maximal conductances.
        E_Na, E_K, E_L: Reversal potentials.
    
    Returns:
        jacobian: Jacobian matrix of the Hodgkin-Huxley model.
    """
    # Calculate the derivatives of gating variables
    dalpha_m = (0.1 * np.exp(0.1 * (V + 35))) / ((np.exp(0.1 * (V + 35)) + 1) ** 2)
    dbeta_m = -np.exp((V + 65) / 18) / 18
    dalpha_h = -0.007 * np.exp((V + 65) / 20)
    dbeta_h = (-0.3 * np.exp(0.1 * (V + 35))) / ((np.exp(0.1 * (V + 35)) + 1) ** 2)
    dalpha_n = (0.01 * np.exp(0.1 * (V + 55))) / ((np.exp(0.1 * (V + 55)) + 1) ** 2)
    dbeta_n = -np.exp((V + 65) / 80) / 80
    
    # Calculate the elements of the Jacobian matrix
    dVdm = -g_Na * h * (V - E_Na)
    dVdh = -g_Na * m ** 3 * (V - E_Na)
    dVdn = -g_K * n ** 4 * (V - E_K)
    dmdV = (eq_parameters.alpha_m(V) * (1 - m) - eq_parameters.beta_m(V) * m) / C_m
    dmdm = -eq_parameters.beta_m(V) - eq_parameters.alpha_m(V)
    dmdh = 0
    dmdn = 0
    dhdV = (eq_parameters.alpha_h(V) * (1 - h) - eq_parameters.beta_h(V) * h) / C_m
    dhdh = -eq_parameters.beta_h(V) - eq_parameters.alpha_h(V)
    dhdn = 0
    dndV = (eq_parameters.alpha_n(V) * (1 - n) - eq_parameters.beta_n(V) * n) / C_m
    dndm = 0
    dndh = 0
    dndn = -eq_parameters.beta_n(V) - eq_parameters.alpha_n(V)
    
    jacobian = np.array([[dVdm, dVdh, dVdn],
                         [dmdV, dmdm, dmdh, dmdn],
                         [dhdV, dhdh, dhdn],
                         [dndV, dndm, dndh, dndn]])
    
    return jacobian



