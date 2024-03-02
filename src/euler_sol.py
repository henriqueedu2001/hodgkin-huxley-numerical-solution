import numpy as np
import pandas as pd
import eq_parameters
import state_variables

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
    
    discretize_domain, delta_t = discretize_interval(time_interval, n_steps)
    
    solution = []
    
    y_aprox = []
    
    # y_0 = y(0)
    y_aprox.append(initial_y)
    
    # evaluates y_{k+1} com y_k e t_k
    for k, t_k in enumerate(discretize_domain[:-1]):
        y_k = y_aprox[k]
        
        # y_{k+1} = y_k + f(t_k, y_k)*delta_t
        next_y = y_k + cauchy_function(t_k, y_k, constants)*delta_t
        y_aprox.append(next_y)
    
    # adds time stamps
    for k, y_k in enumerate(y_aprox):
        t_k = np.array([discretize_domain[k]])
        time_stamped_sol = np.concatenate((t_k, y_k))
        solution.append(time_stamped_sol)
        
    # solution = np.array(solution)
    
    return solution


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
    alpha_n, beta_n = eq_parameters.alpha_m(V), eq_parameters.beta_m(V)
    
    # print(V, I, C, m, h, n, g_Na, g_K, g_L, E_Na, E_K, E_L)
    
    # evaluating the derivatives of each component
    der_v = state_variables.der_Voltage(V, I, C, m, h, n, constants)
    der_m = state_variables.der_m(alpha_m, beta_m, m)
    der_h = state_variables.der_h(alpha_h, beta_h, h)
    der_n = state_variables.der_n(alpha_n, beta_n, n)
    
    der_y = np.array([der_v, der_m, der_h, der_n])
    
    return der_y


def discretize_interval(interval: (float, float), n_steps: int) -> np.array:
    """Discretizes the interval [a, b], in to n points [t_0, t_1, t_2, t_3, ..., t_{n-1}],
    evenly spaced. t_{k+1} = t_k + delta_t, sendo delta_t = (b-a)/n.

    Args:
        interval (float, float): 
        n_steps (int): number os steps

    Returns:
        np.array: the vector of the discretized interval [t_0, t_1, t_2, t_3, ..., t_{n-1}]
        float: step size of the interval
    """
    
    start, stop = interval[0], interval[1]
    step_size = (stop - start)/n_steps
    
    discrete_domain = np.arange(start, stop, step_size)
    
    return discrete_domain, step_size


def main():
    constants = {
        'current': 0., 
        'capacitance':0.1e0,
        'g_Na': 120.,
        'g_K': 36., 
        'g_L': 0.3,
        'E_Na': +24.21, 
        'E_K':  -31.76, 
        'E_L':  -49.0
    }
    
    T = [0, 6]
    n = 12000
    
    y_0 = np.array([
            -65, # V
            0.05,  # m
            0.06,  # h
            0.35   # n
        ])
    
    #print(cauchy_function(0, y_0, constants))
    
    sol = euler_solution(T, n, y_0, constants)
    
    for x in sol:
        print(x)

    df = pd.DataFrame(sol)
    df.to_csv('out.csv')
    
    # print(sol)
    
    # essa parte aqui vai ser mais chatinha de fazer kkkk
    # E_L = -49. 
    # E_Na = R*T*math.log(Na_o/Na_i)/F
    # E_K = R*T*math.log(K_o/K_i)/F

    # F = 96.5                    #Constante de Faraday (coulombs/mmol)
    # R = 8.314                   #COnstante dos gases (J/K)
    # T_celsius = 6.3             #Temperatura a qual é submetido o axônio (em celsius) 
    # T = T_celsius + 273         #Temperatura em K
    
    return

main()
