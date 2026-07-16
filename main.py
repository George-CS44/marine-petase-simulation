import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pef
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

    ax.axvspan(-2, 20, alpha=0.08, color='steelblue', label='Marine surface range(0-20°C)')

    refs = [
        (4, '#0077b6', 'Deep ocean (4°C)'),
        (8 , '#00b4d8', 'Marine surface (8°C)'),
        (17, '#90e0ef', 'Tropical surface (17°C)'),
        (25, '#ef233c', 'Mutant Denaturation (25°C)'),
    ]
    for T_val, color, label in refs:
        ax.axvline(T_val, color=color, linestyle='--', alpha=0.75, linewidth=1.5)
        ax.text(T_val + 0.5, 104, label, rotation=90, fontsize=10,color=color, va='top', ha='left')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Relative Activity (% ofVmax)')
    ax.set_title('Temperature Activity of PETase variants')
    ax.set_xlim(-2, 58)
    ax.set_ylim(0, 115)
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
        (7.9, '#f4a261', 'Projected ocean acidification (7.9)'),
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

def plot_kinetics():
    fig, ax = plt.subplots(figsize=(11, 6))
    S_range = np.linspace(0, 5, 400)
    T_ocean = 8 

    wt_theoretical = michaelis_menten(S_range, WILD_TYPE['Vmax'], WILD_TYPE['Km'])
    mm_theoretical = michaelis_menten(S_range, MARINE_TYPE['Vmax'], MARINE_TYPE['Km'])
    wt_AT_8 = michaelis_menten_temp_scaled(S_range, T_ocean, WILD_TYPE)
    mm_AT_8 = michaelis_menten_temp_scaled(S_range, T_ocean, MARINE_TYPE)

    ax.plot(S_range, wt_theoretical, color=WILD_TYPE['colour'], linestyle='--', alpha=0.4, label='WT Theoretical Max')
    ax.plot(S_range, mm_theoretical, color=MARINE_TYPE['colour'], linestyle='--', alpha=0.4, label='Marine Theoretical Max')
    ax.plot(S_range, wt_AT_8, color=WILD_TYPE['colour'], label='WT at 8°C')
    ax.plot(S_range, mm_AT_8, color=MARINE_TYPE['colour'], label='Marine at 8°C')

    ax.axvspan(0, 0.5, alpha=0.07, color='steelblue', label='Typical ocean PET concentration range (0-0.5 mM)')

    ax.set_xlabel('[PET Substrate] (mM)')
    ax.set_ylabel('Relative Velocity (% of Vmax)')
    ax.set_title('Figure 3: Michaelis-Menten Kinetics of PETase Variants at 8°C')
    ax.set_xlim(0, 5)
    ax.set_ylim(0)
    ax.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig('figures/figure3_kinetics_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')

    plt.show()
    print("Saved Figure3 Kinetics Comparison.png")

def plot_heatmaps():
    T_vals = np.linspace(0, 30, 200)
    pH_vals = np.linspace(7.0, 8.8, 200)

    wt_map = generate_environmental_heatmap(T_vals, pH_vals, WILD_TYPE)
    mm_map = generate_environmental_heatmap(T_vals, pH_vals, MARINE_TYPE)

    ("Temperature °C, pH, label")
    ocean_sites = [
        (8, 8.05, 'North Atlantic Ocean'),
        (28, 8.10, 'Carribean Sea'),
        (1, 8.00, 'Arctic Ocean'),
        (15, 7.60, 'Acidified Ocean'),
    ]
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))
    vmax_val = max(wt_map.max(), mm_map.max())

    for ax, data, enzyme in zip(axs, [wt_map, mm_map], [WILD_TYPE, MARINE_TYPE]):
        im = ax.imshow(
            data,
            aspect='auto',
            origin='lower',
            extent=[T_vals[0], T_vals[-1], pH_vals[0], pH_vals[-1]],
            cmap='YlOrRd',
            vmin=0,
            vmax=vmax_val,
        )
        for T_s, pH_s, site_label in ocean_sites:
            ax.scatter(T_s, pH_s, color='white', edgecolor='black', s=80, zorder=5, linewidth=1.2)
            ax.annotate(
                site_label, (T_s, pH_s),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold', color='weight',
                path_effects=[pef.withStroke(linewidth=2, foreground='black')]
            )
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('pH')
        ax.set_title(enzyme['name'])

    cbar = fig.colorbar(im, ax=axs.tolist(), shrink=0.85, pad=0.02)
    cbar.set_label('Relative Activity (% of Vmax)')
    fig.suptitle('Figure 4: Environmental Heatmaps of PETase Variants', fontsize=13, fontweight='bold')

    plt.tight_layout()
    plt.savefig('figures/figure4_heatmaps.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print("Saved Figure4 Heatmaps.png")

if __name__ == "__main__":
    print("Running Marine PETase Simulation......")
    plot_temperature()
    plot_ph()
    plot_kinetics()
    plot_heatmaps()
    print("All figures generated and saved in'/figures'.")