import numpy as np
from src.temperature_model import activity_vs_temperature
from src.ph_model import activity_vs_ph

params = {
    "Ea": 4200,
    "T_opt": 12,
    "T_den": 25,
    "Vmax": 60,
    "pH_opt": 8.1,
    "pH_sigma": 1.5,
}

def test_arrhenius_at_optimal_temperature():
    assert result == 1.0
def test_ph_returns_positive_activity():
    assert activity_vs_ph(8.1, params) > 0