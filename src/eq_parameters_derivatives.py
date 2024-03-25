import numpy as np

def der_alpha_m(voltage: float) -> float:
    """Computes the alpha_m parameter of the Hodgkin-Huxley model, given
    by alpha_m = 0.1(V + 25)/(e^((V + 25)/10) - 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_m parameter for the specified voltage 
    """
    V = voltage
    
    # auxiliary variables
    aux_1 = 0.1*(np.exp((V + 25)/10) - 1)
    aux_2 = 0.01*(V+25)*np.exp((V + 25)/10)
    aux_3 = (np.exp((V+25)/10) - 1)**2
    
    der_alpha = (aux_1- aux_2)/(aux_3)
    
    return der_alpha


def der_beta_m(voltage: float) -> float:
    """Computes the beta_m parameter of the Hodgkin-Huxley model, given
    by beta_m = 4e^(V/18)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_m parameter for the specified voltage 
    """
    V = voltage
    der_beta = (4/18)*np.exp(-V/18.)
    
    return der_beta


def der_alpha_h(voltage: float) -> float:
    """Computes the alpha_h parameter of the Hodgkin-Huxley model, given
    by alpha_h = 0.07e^(V/20)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_h parameter for the specified voltage 
    """
    V = voltage
    der_alpha = (0.07/20)*np.exp(-V/20.)
    
    return der_alpha


def der_beta_h(voltage: float) -> float:
    """Computes the beta_h parameter of the Hodgkin-Huxley model, given
    by beta_h = 1/(e^((V + 30)/10) + 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_h parameter for the specified voltage 
    """
    V = voltage
    
    aux_1 = -0.1*np.exp((V+30)/10)
    aux_2 = (np.exp((V+30)/10) + 1)**2
    der_beta = -aux_1/aux_2
    
    return der_beta


def der_alpha_n(voltage: float) -> float:
    """Computes the alpha_n parameter of the Hodgkin-Huxley model, given
    by alpha_n = 0.01(V + 10)/(e^((V + 10)/10) - 1)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the alpha_n parameter for the specified voltage 
    """
    V = voltage
    aux_1 = 0.01*(np.exp((V + 10)/10) - 1)
    aux_2 = 0.001*(V + 10)*np.exp((V+10)/10)
    aux_3 = (np.exp((V+10)/10) - 1)**2
    
    der_alpha = (aux_1 - aux_2)/aux_3
    
    return der_alpha


def der_beta_n(voltage: float) -> float:
    """Computes the beta_n parameter of the Hodgkin-Huxley model, given
    by beta_n = 0.125e^(V/80)

    Args:
        voltage (float): voltage V in the neuron

    Returns:
        float: the beta_n parameter for the specified voltage 
    """
    V = voltage
    der_beta = -(0.125/80)*np.exp(-V/80)
    
    return der_beta