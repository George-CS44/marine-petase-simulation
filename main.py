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

WILD_TYPE = {
    'name': 'Wild PETase Type',
    'Ea': 65000,
    'T_opt': 35,
    'T_den': 50,
    'Vmax' : 0.8,
    'pH_opt': 7.5,
    'pH_sigma': 1.5,
    'Km' : 0.8,
    'colour': '#2196F3',
}

MARINE_TYPE = {
    'name': 'Marine PETase Type',
    'Ea': 4200,
    'T_opt': 12,
    'T_den': 25,
    'Vmax' : 60,
    'pH_opt': 8.1,
    'pH_sigma': 0.6,
    'Km' : 0.25,
   'colour': '#4CAF50',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'figure.facecolor': 'white',
    'axes.facecolor': '#f8f9fa',
    'axes.grid': True,
    'grid.alpha': 0.4,
    'lines.linewidth': 2.5,
    'legend.framalpha': 0.9,
})

os.makedirs('figures', exist_ok=True)

def plot_temperature():
    fig, ax = plt.subplots(figsize=(11, 6))
    T_range = np.linspace(-2, 58, 600)

    wt_act = activity_vs_temperature(T_range, WILD_TYPE)
    mm_act = activity_vs_temperature(T_range, MARINE_TYPE)

    ax.plot(T_range, wt_act, label=WILD_TYPE['name'], color=WILD_TYPE['colour'])
    ax.plot(T_range, mm_act, label=MARINE_TYPE['name'], color=MARINE_TYPE['colour'])

    ax.axvspan(-2, 20, aplha=0.08, color='steelblue', label='Marine surface range(0-20°C)')

    refs = [
        (4, '#0077b6', 'Deep ocean (4°C)'),
        (8 , '#00b4d8', 'Marine surface (8°C)'),
        (17, '#90e0ef', 'Tropical surface (17°C)'),
        (25, 'ef233c', 'Mutant Denaturation (25°C)'),
    ]
    for T_val, color, label in refs:
        ax.axvline(T_val, color=color, linestyle='--', alpha=0.75, linewidth=1.5)
        ax.text(T_val + 0.5, 104, label, rotation=90, fontsize=10,color=col, va='top', ha='left')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Relative Activity (% ofVmax)')
    ax.set_title('Temperature Activity of PETase variants')
    ax.set_ylim(-2, 58)
    ax.set_xlim(0, 115)
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig('figures/figure1_temperature_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')

    plt.show()
    print("Saved Figure1 Temperature Comparison.png")

    def plot_ph():
        figr, ax = plt.subplots(figsize=(11, 6))
        pHrange = np.linspace(5.0, 10.5, 400)

        wt_ph = activity_vs_ph(pHrange, WILD_TYPE)
        mm_ph = activity_vs_ph(pHrange, MARINE_TYPE)

        ax.plot(pHrange, wt_ph, label=WILD_TYPE['name'], color=WILD_TYPE['colour'])
        ax.plot(pHrange, mm_ph, label=MARINE_TYPE['name'], color=MARINE_TYPE['colour'])

        acidic_refs = [
            (8.1, '#2d6a4f', 'Ocean surface pH (8.1)'),
            (7.9, 'f4a261', 'Projected ocean acidification (7.9)'),
            (7.5, '#e63946', 'Worst-case pH (7.5)'),
        ]
        for pH_val, color, label in acidic_refs:
            ax.axvline(pH_val, color=color, linestyle='--', alpha=0.8, linewidth=1.5)
            ax.text(pH_val + 0.05, 104, label, rotation=90, fontsize=8,color=color, va='top', ha='left')

        ax.set_xlabel('pH')
        ax.set_ylabel('Relative Activity (% of Vmax)')
        ax.set_title('Figure 2: pH Activity of PETase Wild Type and Marine Type')
        ax.set_xlim(5.0, 10.5)
        ax.set_ylim(0, 115)
        ax.legend(loc='upper right')

        plt.tight_layout()
        plt.savefig('figures/figure2_ph_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
        plt.show()
        print("Saved Figure2 pH Comparison.png")