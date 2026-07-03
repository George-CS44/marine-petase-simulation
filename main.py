import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffect as pef
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.temperature_model import activity_vs_temperature
from src.ph_model import activity_vs_ph
from src.kinetics_model import michaelis_menten, michaelis_menten_temp_scaled
from src.heatmap_model import generate_environmental_heatmap

