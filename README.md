# Marine-PETase-Simulation
# Open in Colab and run cell 1 for dependancies in requiremnets.txt to be installed, in cell 2 adjustments can be made to pH and temp according to limits stated then run to make a graph comparing mutant and wild type percentage activity. Run actual code not in Colab for demonstration of all of the graphs of comparisons.
[![Badge showing Google Colab icon and text Open In Colab for launching the notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/George-CS44/marine-petase-simulation/blob/main/notebooks/full_analysis.ipynb)
# Overview - Computer simulated project of modified cold adapted PETase enzyme kinetics to reduce ocean plastic pollution

Idea behind project-
Marine plastic pollution poses a significant global challenge with few scalable long-term solutions currently available. This simulation presents a theoretical intervention involving the introduction of a modified PETase enzyme into marine ecosystems, designed to catalyze the degradation of polyethylene terephthalate (PET) under conditions that typically inhibit conventional PETase activity. This simulation evaluates the performance of the modified PETase across diverse oceanic environments to identify a viable enzymatic approach to mitigating the threat of microplastic accumulation.

Adaptations-
Conventional Wild-Type PETase possesses a high activation energy barrier, rendering it unfeasible for application in marine temperatures below 20°C. In contrast, the engineered Marine Mutant exhibits a significantly reduced activation energy, enabling active catalysis within these lower temperature ranges. Furthermore, the Marine Mutant maintains structural stability across standard oceanic pH levels (8.0–8.2), whereas the Wild-Type is optimized for distinct terrestrial biochemical environments.

Equations-
Arrhenius equation - k(T) = A . exp(-ea/RT) modeling the temperature-dependent rate constant. Michaelis-Menten Kinetics - V = Vmax[S]/Km+[S] approximating reaction velocity from substrate concentration.

Conclusion-
Ultimately, this project addresses the kinetic bottlenecks that impede the efficiency of Wild-Type PETase within targeted marine environments. By re-engineering an enzyme typically utilized for terrestrial plastic recycling to function under low-temperature and alkaline conditions, this model provides a promising biological strategy for remediating areas where plastic waste accumulates without effective mitigation measures.