import numpy as np

def der_Voltage(
    voltage: float, current: float, capacitance: float, 
    m: float, h: float, n: float,
    g_Na: float, g_K: float, g_L: float,
    E_Na: float, E_K: float, E_L: float) -> float:
    """Computes derivative of the voltage V in the model.
    der_v = ...

    Args:
        voltage (float): voltage V in the neuron
        current (float): the current in the neuron
        m (float): probability of opening activated of sodium channel by voltage
        h (float): probability of opening unactivated of sodium channel by voltage
        n (float): probability of opening unactivated of potassium channel by voltage
        g_Na (float): sodium channel conductance
        g_K (float): potassium channel conductance
        g_L (float): leakage conductance
        E_Na (float): sodium equilibrium potential
        E_K (float): potassium equilibrium potential
        E_L (float): leakage equilibrium potential

    Returns:
        float: the derivative V'(t) of the voltage V(t)
    """
    V = voltage
    C = capacitance
    I = current
    
    derivative_V = (I/C) - g_Na*m**3*h(V - E_Na) - g_K*n**4(V - E_K) - g_L*(V - E_L)

    return derivative_V


def der_m(alfa_m: float, beta_m: float, m: float) -> float:
    """Computes derivative of the probability of opening activated of sodium channel by voltage.
    der_m = alfa_m*(1 - m) - beta_m*m

    Args: 
        alfa_m (float): transition rate of sodium by voltage
        beta_m (float): transition rate of sodium by voltage
        m (float): probability of opening activated of sodium channel by voltage

    Returns:
        float: the derivative of the probability of opening activated of sodium channel by voltage
    """    
    
    return alfa_m*(1 - m) - beta_m*m


def der_h(alfa_h: float, beta_h: float, h: float) -> float:
    """Computes derivative of the probability of opening unactivated of sodium channel by voltage.
    der_h = alfa_h*(1 - h) - beta_h*h

    Args: 
        alfa_h (float): transition rate of sodium by voltage
        beta_h (float): transition rate of sodium by voltage
        h (float): probability of opening unactivated of sodium channel by voltage

    Returns:
        float: the derivative of the probability of opening unactivated of sodium channel by voltage
    """    
    
    return alfa_h*(1-h) - beta_h*h


def der_n(alfa_n: float, beta_n: float, n: float) -> float:
    """Computes the derivative of the probability of potassium channel opening.
    der_n = alfa_n*(1 - n) - beta_n*n

    Args: 
        alfa_n (float): transition rate of potassium by voltage
        beta_n (float): transition rate of potassium by voltage
        n (float): probability of opening unactivated of potassium channel by voltage

    Returns:
        float: the derivative of the probability of opening of potassium channel by voltage
    """    
    
    return alfa_n*(1-n) - beta_n*n