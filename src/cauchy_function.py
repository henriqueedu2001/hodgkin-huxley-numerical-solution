import numpy as np
import pandas as pd
import eq_parameters
import state_variables

def cauchy_function(t: float, y: np.array, constants: dict) -> np.array:
    """The derivative y'(t) = [V'(t), m'(t), h'(t), n'(t)] of the Cauchy's initial problem.

    Args:
        t (float): instante of time t
        y (float): function y in the instant t

    Returns:
        float: the derivative of y'(t) = [V'(t), m'(t), h'(t), n'(t)] in the instante t
    """
    
    # unpacking the parameters from the dictionary "constants"
    I, C = constants['current'], constants['capacitance']
    g_Na, g_K, g_L = constants['g_Na'], constants['g_K'], constants['g_L']
    E_Na, E_K, E_L = constants['E_Na'], constants['E_K'], constants['E_L']
    
    # Getting the values of V, m, h, n in the vector of y
    V, m, h, n = y[0], y[1], y[2], y[3]
    
    # computing the alpha and beta parameters of the model
    alpha_m, beta_m = eq_parameters.alpha_m(V), eq_parameters.beta_m(V)
    alpha_h, beta_h = eq_parameters.alpha_h(V), eq_parameters.beta_h(V)
    alpha_n, beta_n = eq_parameters.alpha_n(V), eq_parameters.beta_n(V)
    
    # print(V, I, C, m, h, n, g_Na, g_K, g_L, E_Na, E_K, E_L)
    
    # evaluating the derivatives of each component
    der_m = state_variables.der_m(alpha_m, beta_m, m)
    der_h = state_variables.der_h(alpha_h, beta_h, h)
    der_n = state_variables.der_n(alpha_n, beta_n, n)
    der_v = state_variables.der_Voltage(V, I, C, m, h, n, constants)
    
    der_y = np.array([der_v, der_m, der_h, der_n])
    
    return der_y


def discretize_interval(interval: (float, float), n_steps: int) -> np.array:
    """Discretizes the interval [a, b], in to n points [t_0, t_1, t_2, t_3, ..., t_{n-1}],
    evenly spaced. t_{k+1} = t_k + delta_t, where delta_t = (b-a)/n.

    Args:
        interval (float, float): 
        n_steps (int): number os steps

    Returns:
        np.array: the vector of the discretized interval [t_0, t_1, t_2, t_3, ..., t_{n-1}]
        float: step size of the interval
    """
    
    start, stop = interval[0], interval[1]
    step_size = (stop - start)/n_steps
    
    discrete_domain = np.linspace(start, stop, n_steps + 1)  # +1 to include the stop point
    
    return discrete_domain, step_size