import numpy as np

def alpha_m(voltage: float) -> float:
    """Computes the alpha_m parameter of the Hodgkin-Huxley model, given
    by alpha_m = 0.1(V + 25)/(e^((V + 25)/10) - 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_m parameter for the specified voltage 
    """
    V = voltage
    alpha = 0.1*(25. - V)/(np.exp((25. - V)/10.) - 1)
    
    return alpha


def beta_m(voltage: float) -> float:
    """Computes the beta_m parameter of the Hodgkin-Huxley model, given
    by beta_m = 4e^(V/18)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_m parameter for the specified voltage 
    """
    V = voltage
    beta = 4.*np.exp(-V/18.)
    
    return beta


def alpha_h(voltage: float) -> float:
    """Computes the alpha_h parameter of the Hodgkin-Huxley model, given
    by alpha_h = 0.07e^(V/20)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_h parameter for the specified voltage 
    """
    V = voltage
    alpha = 0.07*np.exp(-V/20.)
    
    return alpha


def beta_h(voltage: float) -> float:
    """Computes the beta_h parameter of the Hodgkin-Huxley model, given
    by beta_h = 1/(e^((V + 30)/10) + 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_h parameter for the specified voltage 
    """
    V = voltage
    beta = 1./(np.exp((30 - V) / 10) + 1)
    
    return beta


def alpha_n(voltage: float) -> float:
    """Computes the alpha_n parameter of the Hodgkin-Huxley model, given
    by alpha_n = 0.01(V + 10)/(e^((V + 10)/10) - 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_n parameter for the specified voltage 
    """
    V = voltage
    alpha = 0.01*(10 - V)/(np.exp((10 - V) / 10) - 1)
    
    return alpha


def beta_n(voltage: float) -> float:
    """Computes the beta_n parameter of the Hodgkin-Huxley model, given
    by beta_n = 0.125e^(V/80)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_n parameter for the specified voltage 
    """
    V = voltage
    beta = 0.125*np.exp(-V/80)
    
    return beta