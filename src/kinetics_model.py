import numpy as np
from src.temperature_model import activity_vs_temperature

def michaelis_menten(Sub, Vmax, Km):
    return (Vmax * Sub) / (Km + Sub)

def michaelis_menten_temp_scaled(Sub, T_celsius, params):
    effective_Vmax = activity_vs_temperature(T_celsius, params)
    return michaelis_menten(Sub, effective_Vmax, params['Km'])