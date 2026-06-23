import numpy as np
R = 8.314
def arrhenius_equation(T_celsius, Ea, T_opt_celsius):
    T = T_celsius + 273.15
    T_opt = T_opt_celsius + 273.15
    return  np.exp(-Ea / (R * T)) * np.exp(Ea / (R * T_opt))