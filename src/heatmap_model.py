import numpy as np
from src.temperature_model import activity_vs_temperature
from src.ph_model import activity_vs_ph

def gen_environmental_heatmap(T_vals, pH_vals, params): # Grid of temperature and pH values
    T_grid, pH_grid = np.meshgrid(T_vals, pH_vals)
    T_act = activity_vs_temperature(T_grid, params)
    pH_act = activity_vs_ph(pH_grid, params)
    # Normalize the activity values to the value of Vmax
    t_normal = T_act / params['Vmax']
    pH_normal = pH_act / params['Vmax']
    return params['Vmax'] * t_normal * pH_normal