import numpy as np
R = 8.314 # Universal gas constant in J/(mol*K)
def arrhenius_equation(T_celsius, Ea, T_opt_celsius):
    T = T_celsius + 273.15
    T_opt = T_opt_celsius + 273.15
    return  np.exp(-Ea / (R * T)) * np.exp(Ea / (R * T_opt))
def denature_factor(T_celsius, T_den_celsius, kappa=0.8):
    T = T_celsius + 273.15
    T_den = T_den_celsius + 273.15
    return 1.0 / (1. + np.exp(kappa * (T - T_den)))
def activity_vs_temperature(T_celsius, params):
    arr = arrhenius_normalised(T_celsius, params['Ea'], params['T_opt'])
    den = denature_factor(T_celsius, params['T_den'])
    return params['Vmax'] * arr * den