from src.temperature_model import activity_vs_temperature
from src.ph_model import activity_vs_ph

params = {
    "Ea": 4200,
    "T_opt": 12,
    "T_den": 25,
    "Vmax": 60,
    "pH_opt": 8.1,
    "sigma": 0.6,
    "Km": 0.25,
}

def test_temperature_returns_positive_activity():
    assert activity_vs_temperature(12, params) > 0

def test_ph_returns_positive_activity():
    assert activity_vs_ph(8.1, params) > 0