import numpy as np
from src.temperature_model import acivity_vs_temperature
from src.ph_model import acivity_vs_ph

def gen_enviromental_heatmapT_val, pH_vals, parmas):
    T_grid, pH_grid = np.meshgrid(T_vals, pH_vals)
    T_act = acivity_vs_temperature(T_grid, parmas)
    pH_act = acivity_vs_ph(pH_grid, parmas)
    t_normal = T_act / params['Vmax']
    pH_normal = pH_act / params['Vmax']
    return params['Vmax'] * t_normal * pH_normal