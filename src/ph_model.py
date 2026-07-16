import numpy as np

def activity_vs_ph(pH, params):
    return params['Vmax'] * np.exp(-((pH - params['pH_opt'])**2) / (2 * params['pH_sigma']**2))