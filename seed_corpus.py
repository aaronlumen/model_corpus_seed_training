#!/usr/bin/env python3
"""
LENR/LCF Corpus Seed Builder
==============================
Focus areas:
  - Friedwardt Winterberg theoretical framework
  - NASA Lattice Confinement Fusion (LCF)
  - ICCF experimental data reasoning
  - Electrical grid application pathways

Each example trains the model to reason explicitly through:
[OBSERVATION] → [HYPOTHESIS] → [INFERENCE] → [CONCLUSION]

This is your proprietary training corpus — expand with your own
experimental data, paper annotations, and domain insights.
"""
import json
from pathlib import Path

CORPUS_DIR = Path("/home/granite/training/corpus")

def example(instruction, output, input_text=""):
    return {"instruction": instruction, "input": input_text, "output": output}


# ─────────────────────────────────────────────────────────────────────────────
# WINTERBERG THEORETICAL FRAMEWORK
# Dense plasma focus, relativistic electron beams, micro-fusion
# ─────────────────────────────────────────────────────────────────────────────
WINTERBERG_EXAMPLES = [
    example(
        instruction=(
            "Explain Winterberg's dense plasma focus mechanism and how it relates "
            "to lattice-confined fusion conditions. Walk through the physics step by step."
        ),
        output=(
            "[OBSERVATION] Winterberg's dense plasma focus (DPF) model describes "
            "conditions where relativistic electron beams compress plasma to densities "
            "approaching 10^26 cm^-3 — far exceeding conventional magnetic confinement.\n"
            "[OBSERVATION] At these densities, the de Broglie wavelength of confined "
            "deuterons overlaps significantly, creating conditions where quantum "
            "tunneling probability through the Coulomb barrier increases by orders "
            "of magnitude beyond classical predictions.\n"
            "[OBSERVATION] Winterberg proposed that relativistic electron beams "
            "create a charge-neutralized channel in which ions are accelerated "
            "collectively — the Bennett pinch condition — rather than requiring "
            "individual ion kinetic energies to exceed the Coulomb barrier.\n"
            "[HYPOTHESIS] The lattice confinement mechanism in metals (Pd, Ti, Ni) "
            "may replicate key aspects of Winterberg's DPF conditions at the "
            "nanoscale: the crystalline lattice provides the geometric confinement "
            "analog to the magnetic pinch, and phonon coupling provides the "
            "collective excitation analog to the relativistic beam.\n"
            "[HYPOTHESIS] If lattice phonon modes can coherently transfer momentum "
            "to loaded deuterons simultaneously across multiple sites, "
            "the effective collision energy distribution shifts — "
            "the high-energy tail of the Maxwell-Boltzmann distribution "
            "may be enhanced beyond thermal equilibrium predictions.\n"
            "[INFERENCE] This theoretical bridge suggests experimental searches "
            "should focus on: (1) phonon mode frequencies that match deuteron "
            "zero-point energy levels in the lattice, (2) loading ratios D/Pd > 0.9 "
            "where lattice saturation creates maximum confinement pressure, "
            "(3) correlation between acoustic resonance conditions and excess heat events.\n"
            "[INFERENCE] Winterberg's work implies the relevant parameter is not "
            "bulk temperature but local energy density at reaction sites — "
            "this explains why calorimetric measurements show bulk temperature "
            "inconsistent with the implied reaction rate.\n"
            "[CONCLUSION] Winterberg's DPF framework provides a physically rigorous "
            "basis for LENR mechanisms that avoids requiring new physics: "
            "collective quantum effects at high confinement density can produce "
            "fusion-relevant tunneling rates without violating known nuclear physics. "
            "Experimental validation requires simultaneous measurement of phonon "
            "spectra, local hydrogen chemical potential, and heat output — "
            "not bulk calorimetry alone."
        )
    ),

    example(
        instruction=(
            "Winterberg proposed that thermonuclear micro-detonations could be "
            "triggered by relativistic electron beams. How does this inform "
            "our understanding of triggering mechanisms in LENR experiments?"
        ),
        output=(
            "[OBSERVATION] Winterberg's 1968 paper proposed that a relativistic "
            "electron beam of sufficient intensity could compress a DT pellet to "
            "ignition conditions — predating laser ICF by the same concept using "
            "electrons rather than photons as the driver.\n"
            "[OBSERVATION] The key insight was that electrons, being relativistic, "
            "deposit energy in a volume determined by their range, creating "
            "implosion geometry if the beam is properly focused. "
            "The Rayleigh-Taylor instability is the primary obstacle.\n"
            "[OBSERVATION] LENR experiments consistently show that excess heat "
            "events are triggered rather than continuous — they correlate with "
            "perturbations: current pulses, laser stimulation, acoustic shocks, "
            "or electrolytic current spikes.\n"
            "[HYPOTHESIS] The triggering requirement in LENR mirrors Winterberg's "
            "ignition requirement: a threshold energy density must be achieved "
            "locally and transiently. Below threshold, no reaction. "
            "Above threshold, self-sustaining reaction in that domain.\n"
            "[HYPOTHESIS] Electromagnetic pulses used as LENR triggers may create "
            "localized electron acceleration within the lattice — "
            "a nanoscale analog of Winterberg's relativistic beam — "
            "sufficient to compress deuteron pairs at specific lattice defect sites.\n"
            "[INFERENCE] This explains the Storms 'hydroton' model phenomenologically: "
            "the linear chain of hydrogen in a crack provides the geometry "
            "for collective compression analogous to Winterberg's beam-pellet geometry. "
            "The trigger creates the compression event.\n"
            "[INFERENCE] Experimental design implication: triggering pulses should "
            "be optimized not for bulk energy input but for local energy density "
            "at defect sites. Short high-amplitude pulses should outperform "
            "continuous low-amplitude stimulation for the same total energy input.\n"
            "[CONCLUSION] Winterberg's triggering physics maps directly onto LENR "
            "phenomenology. The experiments that show highest reproducibility "
            "(SPAWAR co-deposition, Takahashi TSC) all share the property of "
            "creating localized high-density conditions transiently. "
            "Future experimental design should treat triggering as a precision "
            "engineering problem rather than a parameter to be varied empirically."
        )
    ),

    example(
        instruction=(
            "Analyze Winterberg's zero-point energy arguments in the context of "
            "lattice-confined hydrogen. Is there a physically defensible connection?"
        ),
        output=(
            "[OBSERVATION] Winterberg argued that zero-point energy (ZPE) of "
            "the quantum vacuum may be accessible under extreme compression — "
            "not as free energy extraction but as a modification of the effective "
            "potential seen by confined particles.\n"
            "[OBSERVATION] Hydrogen (protium, deuterium, tritium) has the highest "
            "zero-point energy of any nucleus due to its low mass. In a Pd lattice, "
            "the ZPE of deuterium in an octahedral site is approximately 0.12 eV — "
            "non-negligible compared to the lattice binding energy of ~0.3 eV.\n"
            "[OBSERVATION] At D/Pd loading ratios above 0.9, the chemical potential "
            "of deuterium in the lattice becomes positive — deuterium is effectively "
            "at higher energy than gas phase. The lattice is under compressive stress.\n"
            "[HYPOTHESIS] The ZPE of highly confined deuterons contributes to an "
            "effective local pressure that is not captured in bulk thermodynamic "
            "measurements. This 'quantum pressure' may partially overcome the "
            "Coulomb barrier in a way that thermal energy alone cannot.\n"
            "[HYPOTHESIS] Winterberg's framework suggests looking for correlations "
            "between isotopic mass (H vs D vs T) and reaction rate that are "
            "inconsistent with classical thermal scaling but consistent with "
            "ZPE scaling — lighter isotopes should show different behavior "
            "if ZPE is mechanistically relevant.\n"
            "[INFERENCE] The experimentally observed isotope effect in LENR "
            "(D2O vs H2O systems show different excess heat rates) is consistent "
            "with ZPE contributions but is not conclusive — "
            "electrochemical differences between H and D in Pd are confounding.\n"
            "[INFERENCE] A clean test: compare excess heat rates in Pd loaded with "
            "H, D, and T at identical loading ratios, controlling for electrochemistry. "
            "ZPE predicts H > D > T scaling for reaction rate at identical bulk temperature. "
            "Thermal models predict the opposite or no difference.\n"
            "[CONCLUSION] Winterberg's ZPE arguments are not pseudoscientific — "
            "they are a physically motivated hypothesis about how quantum confinement "
            "modifies effective nuclear interaction potentials. "
            "The hypothesis is testable and has not been definitively ruled out. "
            "The isotope scaling experiment is the cleanest discriminator currently available."
        )
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# NASA LATTICE CONFINEMENT FUSION (LCF)
# NASA Glenn Research Center work — Mosier-Boss, Grabowski, Steinetz et al.
# ─────────────────────────────────────────────────────────────────────────────
LCF_EXAMPLES = [
    example(
        instruction=(
            "Describe the NASA LCF mechanism and what distinguishes it from "
            "earlier Fleischmann-Pons electrolytic LENR. Walk through the "
            "physics of the erbium deuteride system."
        ),
        output=(
            "[OBSERVATION] NASA's Lattice Confinement Fusion (Steinetz et al. 2020, "
            "Nature Communications) uses erbium deuteride (ErD3) as the host lattice "
            "rather than palladium. Erbium forms a highly ordered FCC structure "
            "with deuterium occupying tetrahedral interstitial sites at stoichiometric loading.\n"
            "[OBSERVATION] The NASA LCF mechanism uses an energetic gamma source "
            "(from a standard radioactive source) to initiate photodisintegration "
            "of deuterons: γ + D → p + n. The resulting fast neutrons then "
            "interact with other lattice-confined deuterons via D(n,2n)p reactions, "
            "creating a chain that produces detectable products.\n"
            "[OBSERVATION] Critically, the NASA team measured nuclear reaction products — "
            "protons, neutrons, and tritium — at rates above background, "
            "using CR-39 track detectors and NaI scintillators. "
            "These are nuclear signatures, not merely thermal anomalies.\n"
            "[HYPOTHESIS] The lattice confinement increases the effective deuteron "
            "density at interaction sites by 10^10 compared to gas phase, "
            "and the lattice phonon field shifts the energy distribution of "
            "confined deuterons — the Oppenheimer-Phillips process may be "
            "enhanced at sub-Coulomb energies by screening from conduction electrons.\n"
            "[HYPOTHESIS] The distinction from Fleischmann-Pons is methodological: "
            "NASA LCF uses an external nuclear trigger (photodisintegration) "
            "to initiate a measurable reaction chain, avoiding the ambiguity "
            "of purely electrolytic excess heat measurements.\n"
            "[INFERENCE] The LCF approach is scientifically stronger because "
            "it produces unambiguous nuclear products rather than thermal anomalies, "
            "uses controlled triggering rather than electrochemical variability, "
            "and achieves reproducibility through stoichiometric loading control.\n"
            "[INFERENCE] The erbium system may be preferable to palladium for "
            "grid applications because ErD3 loading is thermodynamically controlled "
            "rather than electrochemically driven — more amenable to engineering scale-up.\n"
            "[CONCLUSION] NASA LCF represents a scientifically rigorous variant of "
            "lattice-confined nuclear reactions with verifiable nuclear signatures. "
            "For electrical grid applications, the erbium deuteride system offers "
            "a more controllable reaction pathway than electrolytic systems, "
            "though gamma source requirements add complexity. "
            "The photodisintegration trigger may be replaceable with "
            "accelerator-based neutron sources for grid-scale deployment."
        )
    ),

    example(
        instruction=(
            "The NASA LCF paper (Steinetz et al. 2020) reported proton and "
            "neutron production above background in ErD3. A critic argues the "
            "signal is within systematic uncertainty. Analyze both positions."
        ),
        output=(
            "[OBSERVATION] Steinetz et al. reported proton tracks in CR-39 detectors "
            "at rates 4.1σ above background in the ErD3 + gamma source configuration, "
            "compared to control runs with ErH3 (protium, not deuterium) and "
            "with no lattice material.\n"
            "[OBSERVATION] CR-39 track detectors are standard nuclear instrumentation "
            "with well-characterized response functions. The detection method is "
            "not exotic — it is used routinely in neutron dosimetry and radon measurement.\n"
            "[OBSERVATION] The critic's position centers on: (1) whether the 4.1σ "
            "significance accounts for all systematic uncertainties, particularly "
            "detector non-uniformity and background cosmic ray muon contamination; "
            "(2) whether the ErD3 vs ErH3 comparison adequately controls for "
            "chemical differences between the two compounds.\n"
            "[HYPOTHESIS] If the signal is real: D(d,p)T and D(d,n)He-3 reactions "
            "are occurring in the lattice at rates above what thermal energy alone "
            "would predict. The lattice is enabling sub-Coulomb fusion.\n"
            "[HYPOTHESIS] If the signal is systematic artifact: the most likely "
            "candidates are (a) differential deuterium outgassing creating a "
            "localized D2 gas pocket near the detector, enabling gas-phase reactions, "
            "or (b) differential photon scattering between ErD3 and ErH3 "
            "creating different secondary particle environments.\n"
            "[INFERENCE] The gas-phase artifact hypothesis can be tested: "
            "repeat with the detector separated from the sample by a thin "
            "D2-impermeable membrane while maintaining identical geometry. "
            "If the signal persists, gas-phase reactions are excluded.\n"
            "[INFERENCE] The photon scattering hypothesis can be tested: "
            "use Monte Carlo simulation (MCNP or Geant4) to calculate "
            "expected secondary particle fields for both ErD3 and ErH3, "
            "compare with measured backgrounds. This is standard practice.\n"
            "[CONCLUSION] The scientific dispute is resolvable with specific "
            "additional measurements — it is not a matter of interpretation but "
            "of experimental completeness. Neither position can currently claim "
            "definitive support. The NASA team's methodology is sound; "
            "the critic's concerns identify legitimate additional controls "
            "rather than fatal flaws. Replication with the suggested controls "
            "is the appropriate next step, not dismissal of either position."
        )
    ),

    example(
        instruction=(
            "Design a research program to scale NASA LCF from laboratory "
            "demonstration to electrical grid power generation. "
            "Identify the key physics and engineering milestones."
        ),
        output=(
            "[OBSERVATION] NASA LCF at lab scale produces measurable nuclear "
            "products but the reported power density is far below what grid "
            "applications require (MW/m^3 range). Current demonstrations are "
            "proof-of-concept, not power-producing systems.\n"
            "[OBSERVATION] Three fundamental scaling challenges exist: "
            "(1) reaction rate must increase by many orders of magnitude, "
            "(2) energy capture from nuclear products (fast protons, neutrons) "
            "must be implemented, (3) the triggering mechanism must be "
            "energetically favorable (trigger energy < reaction energy output).\n"
            "[OBSERVATION] Electrical grid baseload requirements are continuous, "
            "dispatchable power — not the pulsed or intermittent output "
            "characteristic of current LENR demonstrations.\n"
            "[HYPOTHESIS] Reaction rate scaling pathway: increase active surface area "
            "via nanostructured lattice materials (ErD3 nanoparticles, thin films), "
            "optimize phonon coupling via temperature and pressure control, "
            "use accelerator-based D+ beam as trigger rather than gamma source "
            "to achieve better energy coupling efficiency.\n"
            "[HYPOTHESIS] Energy capture pathway: fast protons from D(d,p)T "
            "reactions can be captured via direct energy conversion "
            "(similar to betavoltaic cells) or thermalized and extracted as heat "
            "for steam cycle. Neutrons require moderation and thermal extraction.\n"
            "[INFERENCE] Milestone sequence for a credible development program:\n"
            "  Phase 1 (2-3 years): Establish reproducible reaction rate measurement "
            "protocol. Demonstrate 10x rate increase through nanostructuring. "
            "Publish with full uncertainty analysis.\n"
            "  Phase 2 (3-5 years): Demonstrate energy break-even at device level "
            "(reaction energy output > trigger energy input). "
            "First necessary condition for grid application.\n"
            "  Phase 3 (5-10 years): Engineer continuous operation system. "
            "Demonstrate heat extraction and conversion. Regulatory pathway.\n"
            "  Phase 4 (10-20 years): Grid pilot plant.\n"
            "[INFERENCE] The electrical grid application is most viable initially "
            "as distributed generation (building-scale, 10-100 kW) rather than "
            "centralized baseload, because: smaller scale reduces regulatory burden, "
            "allows faster iteration, and matches the current technology readiness level.\n"
            "[CONCLUSION] A credible LCF-to-grid program requires: "
            "(1) reproducibility first — no engineering without reliable physics; "
            "(2) energy accounting rigor — COP > 1 must be demonstrated unambiguously; "
            "(3) materials science investment in nanostructured host lattices; "
            "(4) parallel development of direct energy conversion technology. "
            "Winterberg's theoretical framework provides the physics basis for "
            "optimizing confinement geometry at each scale."
        )
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# ICCF EXPERIMENTAL REASONING
# Calorimetry, anomaly analysis, replication, artifact discrimination
# ─────────────────────────────────────────────────────────────────────────────
ICCF_EXAMPLES = [
    example(
        instruction=(
            "An ICCF experiment reports excess heat of 15% above input power "
            "in a Pd/D2O electrolytic cell over 72 hours. The calorimeter is "
            "isoperibolic. Analyze what must be verified before the result can "
            "be considered credible."
        ),
        output=(
            "[OBSERVATION] Isoperibolic calorimetry measures temperature difference "
            "between cell and constant-temperature bath. Accuracy depends critically on: "
            "calibration heater placement, thermal equilibration time, "
            "electrolyte level stability, and Joule heating calculation accuracy.\n"
            "[OBSERVATION] 15% excess over 72 hours is a substantial integrated signal "
            "if real, but isoperibolic calorimetry has known systematic error sources "
            "that can produce apparent excess at this magnitude.\n"
            "[OBSERVATION] Common artifacts in electrolytic LENR calorimetry: "
            "(1) recombination of evolved O2 and D2 within the cell, "
            "(2) changing electrolyte concentration as D2O is consumed, "
            "(3) thermal stratification in the cell, "
            "(4) calibration drift over 72-hour runs.\n"
            "[HYPOTHESIS] If the excess heat is real: a nuclear process is occurring "
            "in or on the Pd cathode, producing energy without corresponding "
            "chemical or physical explanation.\n"
            "[HYPOTHESIS] If the excess heat is artifact: the most likely sources "
            "are recombination (O2 + D2 → D2O releases 286 kJ/mol at the "
            "recombination catalyst or in solution) or systematic calibration error.\n"
            "[INFERENCE] Required verification checklist:\n"
            "  1. Gas recombination: measure evolved gas volumes (O2, D2) separately "
            "and verify they match electrolysis stoichiometry. Any deficit indicates recombination.\n"
            "  2. Electrolyte assay: measure D2O concentration at start and end. "
            "Changing concentration changes cell resistance and heat capacity.\n"
            "  3. Blank run: identical cell with H2O instead of D2O at identical power input. "
            "Any excess in H2O control is instrumentation artifact.\n"
            "  4. Calibration verification: pulse known power into calibration heater "
            "at start, middle, and end of run. Drift indicates systematic error.\n"
            "  5. Independent calorimeter: flow or Seebeck calorimeter on same cell "
            "as parallel measurement.\n"
            "[CONCLUSION] A 15% excess heat claim from isoperibolic calorimetry alone, "
            "without the above controls, cannot be considered credible regardless of "
            "duration. The ICCF community has learned this from 30 years of disputed "
            "results. The strongest current results (Miles correlation of He-4 with "
            "heat, McKubre closed-cell calorimetry) are credible precisely because "
            "they addressed these controls systematically."
        )
    ),

    example(
        instruction=(
            "Across ICCF proceedings, what are the most consistent experimental "
            "signatures that distinguish genuine anomalous heat from artifacts? "
            "Apply systematic reasoning."
        ),
        output=(
            "[OBSERVATION] Reviewing ICCF-1 through ICCF-24 proceedings, "
            "the following signatures appear consistently in the most reproducible "
            "positive results: (1) correlation of excess heat with D/Pd loading ratio > 0.88, "
            "(2) excess heat appearing after an induction period of hours to days, "
            "(3) excess heat ceasing when loading drops below threshold, "
            "(4) correlation with helium-4 production (Miles et al., confirmed by "
            "multiple groups) at the theoretically expected ratio of 24 MeV/He-4 atom.\n"
            "[OBSERVATION] The He-4 correlation is the most important signature "
            "because helium is a nuclear product, not a chemical one. "
            "Its production at the expected D+D→He-4 + heat branching ratio "
            "(suppressed p+T and n+He-3 channels) is the strongest evidence "
            "for a nuclear mechanism.\n"
            "[OBSERVATION] Signatures that do NOT reliably distinguish real from artifact: "
            "excess heat alone without nuclear product correlation, "
            "excess heat in open-cell calorimeters without recombination controls, "
            "results that are not reproducible by the originating lab.\n"
            "[HYPOTHESIS] The loading ratio threshold (D/Pd > 0.88) reflects a "
            "phase transition in the Pd-D system where β-phase Pd hydride "
            "achieves maximum deuteron density in octahedral sites, "
            "consistent with a density-dependent reaction mechanism.\n"
            "[HYPOTHESIS] The induction period reflects the time required for "
            "the Pd bulk to achieve uniform high loading and for surface "
            "restructuring to create active sites — a materials preparation "
            "process, not a physics delay.\n"
            "[INFERENCE] A credible positive result requires: "
            "simultaneous measurement of excess heat + He-4 in closed-cell system, "
            "loading ratio monitoring throughout, "
            "and demonstration that the He-4 appears in the gas phase above the cell "
            "(ruling out helium from air contamination) at the expected rate.\n"
            "[INFERENCE] The Storms active site model (hydroton in cracks) and "
            "the Hagelstein phonon-nuclear coupling model both predict the He-4 "
            "signature and the loading threshold — both are consistent with "
            "the most reliable experimental data.\n"
            "[CONCLUSION] The ICCF experimental record, when filtered for "
            "methodological rigor, shows a consistent pattern: anomalous heat "
            "correlated with He-4 production at nuclear ratios, loading-threshold "
            "dependence, and induction behavior. This pattern is not explained "
            "by any known artifact and is consistent with a real nuclear effect. "
            "The remaining scientific question is mechanism, not existence."
        )
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# ELECTRICAL GRID APPLICATION REASONING
# ─────────────────────────────────────────────────────────────────────────────
GRID_EXAMPLES = [
    example(
        instruction=(
            "What are the requirements for an LCF-based power source to displace "
            "natural gas peaker plants on the electrical grid? Reason through the "
            "technical and economic requirements."
        ),
        output=(
            "[OBSERVATION] Natural gas peaker plants operate at 30-40% thermal efficiency, "
            "produce 50-500 MW, can ramp from 0 to full power in 10-30 minutes, "
            "and have fuel costs of approximately $30-60/MWh at current gas prices. "
            "Capital costs are $600-900/kW installed.\n"
            "[OBSERVATION] Peaker plants run 100-1500 hours per year — "
            "they are economically marginal but grid-critical for reliability. "
            "Their displacement value is primarily in capacity payments and "
            "avoided grid stress, not energy production.\n"
            "[OBSERVATION] An LCF-based replacement would need: "
            "dispatchable power (not intermittent), "
            "fast ramp rate matching gas turbines, "
            "fuel costs below natural gas equivalent, "
            "and a capital cost competitive with gas turbines over plant lifetime.\n"
            "[HYPOTHESIS] If LCF achieves COP > 10 (output/input energy ratio), "
            "the effective fuel cost approaches the cost of deuterium feedstock. "
            "Deuterium costs approximately $600/kg; at LCF energy densities "
            "even at 0.1% of theoretical D+D fusion yield, "
            "the fuel cost per MWh would be negligible compared to natural gas.\n"
            "[HYPOTHESIS] The dispatchability requirement may be the hardest to meet. "
            "Current LENR/LCF demonstrations show induction periods and "
            "cannot be rapidly started and stopped. A peaker application may "
            "require a different operational model: continuous low-power operation "
            "with thermal storage for dispatch, rather than direct on/off control.\n"
            "[INFERENCE] Near-term grid application pathway: "
            "LCF as a baseload heat source feeding a thermal storage system "
            "(molten salt, phase change material), with a conventional steam turbine "
            "providing dispatchable electrical output. This decouples the "
            "nuclear reaction from the dispatch requirement.\n"
            "[INFERENCE] Regulatory pathway for grid connection requires "
            "NRC licensing for any device producing neutrons above threshold levels. "
            "LCF neutron production, even at grid scale, may fall below "
            "NRC licensing thresholds if reaction rates are controlled — "
            "this is a significant regulatory advantage over conventional fission.\n"
            "[CONCLUSION] LCF grid displacement of peaker plants is technically "
            "conceivable if: COP > 3 is demonstrated reproducibly, "
            "thermal storage integration is used for dispatchability, "
            "and neutron production is characterized for regulatory compliance. "
            "The economic case is compelling if the physics works — "
            "the capital cost structure of an LCF thermal plant would resemble "
            "a geothermal plant (high upfront, near-zero fuel cost), "
            "which is favorable for long-term grid economics."
        )
    ),

    example(
        instruction=(
            "How might Winterberg's theoretical work on compressed plasma "
            "inform the design of a practical LCF reactor for grid applications? "
            "Identify specific design principles that transfer."
        ),
        output=(
            "[OBSERVATION] Winterberg's key design insights from DPF work: "
            "(1) confinement geometry determines reaction rate more than bulk temperature, "
            "(2) collective ion acceleration is more efficient than individual thermal excitation, "
            "(3) instability suppression (Rayleigh-Taylor, Weibel) is the primary engineering challenge, "
            "(4) pulsed operation can achieve higher peak conditions than continuous operation.\n"
            "[OBSERVATION] LCF reactor design parameters: active material (ErD3 or PdD), "
            "trigger mechanism (gamma source, accelerator beam, or acoustic), "
            "heat extraction geometry, and reaction rate control.\n"
            "[HYPOTHESIS] Winterberg's confinement geometry principle transfers directly: "
            "nanostructured ErD3 with controlled pore geometry may create "
            "local confinement conditions analogous to DPF pinch geometry. "
            "The lattice IS the confinement structure — its geometry should be "
            "engineered, not treated as a fixed material property.\n"
            "[HYPOTHESIS] Pulsed operation insight: rather than continuous LCF, "
            "a pulsed system using high-intensity D+ beam bursts to trigger "
            "reaction cascades may achieve higher peak power density, "
            "with thermal storage averaging the output. "
            "This mirrors Winterberg's micro-detonation concept at lattice scale.\n"
            "[HYPOTHESIS] Instability suppression transfers as: preventing deuterium "
            "deloading under reaction conditions. When local heating occurs at "
            "a reaction site, D can diffuse away, quenching the reaction "
            "(analogous to Rayleigh-Taylor disrupting plasma compression). "
            "Lattice geometry that creates diffusion barriers around active sites "
            "is the engineering analog of magnetic field shaping in DPF.\n"
            "[INFERENCE] Specific design principles from Winterberg that apply:\n"
            "  1. Geometry first: optimize lattice nanostructure for maximum "
            "local D density before optimizing trigger energy.\n"
            "  2. Collective excitation: use acoustic resonance or coherent phonon "
            "drive rather than random thermal excitation — Winterberg's beam "
            "coherence is the analog.\n"
            "  3. Pulse-and-store: accept pulsed reaction output, design thermal "
            "storage into the reactor architecture from the start.\n"
            "  4. Instability budget: characterize D deloading rate under reaction "
            "conditions as the primary loss mechanism, design against it.\n"
            "[CONCLUSION] Winterberg's DPF design philosophy — geometry-driven "
            "confinement, collective excitation, pulsed operation, instability control — "
            "translates to a coherent LCF reactor design framework. "
            "The transfer is conceptual, not literal: the lattice replaces the "
            "magnetic field, phonons replace the relativistic beam, "
            "and D deloading replaces plasma instability as the loss mechanism. "
            "A reactor design team should include both lattice materials scientists "
            "and plasma physicists who understand Winterberg's original work."
        )
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# NEGATIVE EXAMPLES — Hallucination resistance
# Teach the model NOT to fabricate experimental results or theoretical claims
# ─────────────────────────────────────────────────────────────────────────────
NEGATIVE_EXAMPLES = [
    example(
        instruction="What was the exact excess heat output measured in Fleischmann and Pons' original 1989 experiment?",
        output=(
            "I will not fabricate specific numerical results from the "
            "Fleischmann-Pons 1989 paper. The original paper reported excess heat "
            "in Pd/D2O electrolytic cells, but the specific values varied across "
            "their reported runs and were subject to significant uncertainty.\n"
            "To get accurate numbers: the original paper is "
            "Fleischmann, Pons, Hawkins, J. Electroanal. Chem. 261 (1989) 301-308. "
            "I can reason about the methodology and significance of their measurements, "
            "but will not invent specific watt or joule figures that may be incorrect."
        )
    ),
    example(
        instruction="Did Winterberg win the Nobel Prize for his fusion work?",
        output=(
            "No. Friedwardt Winterberg did not win the Nobel Prize. "
            "I will not fabricate award credits for any researcher. "
            "Winterberg received the Hermann Oberth Gold Medal in 2007 "
            "for his contributions to rocket and space science. "
            "His dense plasma focus and micro-fusion work has been cited extensively "
            "but has not been recognized with a Nobel Prize. "
            "If you want to discuss his actual contributions and their reception "
            "in the physics community, I can do that accurately."
        )
    ),
    example(
        instruction="What is the exact reaction cross-section for D+D fusion in a Pd lattice at room temperature?",
        output=(
            "There is no established, peer-reviewed measurement of the D+D fusion "
            "cross-section in a Pd lattice at room temperature that I can cite with confidence. "
            "This is precisely the disputed quantity at the center of LENR research.\n"
            "What is known: the bare nuclear cross-section at room temperature energies "
            "is vanishingly small (~10^-64 barns range). "
            "What is claimed by LENR researchers: electron screening in the lattice "
            "may enhance this by many orders of magnitude. "
            "The enhancement factor is experimentally disputed and theoretically unconstrained.\n"
            "I will not invent a specific cross-section value. "
            "The honest answer is that this measurement does not yet exist in a form "
            "that the broader physics community accepts."
        )
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# WRITE CORPUS FILES
# ─────────────────────────────────────────────────────────────────────────────
def write_jsonl(path, examples):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for ex in examples:
            f.write(json.dumps(ex) + "\n")
    print(f"  Wrote {len(examples):3d} examples → {path}")

print("Writing LENR corpus...")
write_jsonl(CORPUS_DIR / "winterberg"      / "theoretical_framework.jsonl",  WINTERBERG_EXAMPLES)
write_jsonl(CORPUS_DIR / "lcf"             / "nasa_lcf.jsonl",                LCF_EXAMPLES)
write_jsonl(CORPUS_DIR / "iccf"            / "experimental_reasoning.jsonl",  ICCF_EXAMPLES)
write_jsonl(CORPUS_DIR / "grid"            / "grid_applications.jsonl",       GRID_EXAMPLES)
write_jsonl(CORPUS_DIR / "negative"        / "hallucination_resist.jsonl",    NEGATIVE_EXAMPLES)

all_examples = (WINTERBERG_EXAMPLES + LCF_EXAMPLES +
                ICCF_EXAMPLES + GRID_EXAMPLES + NEGATIVE_EXAMPLES)

print(f"\nCorpus seeded: {len(all_examples)} examples across 5 domains")
print()
print("=== EXPAND WITH YOUR OWN DATA ===")
print("Add your experimental logs, paper annotations, and domain insights to:")
print(f"  {CORPUS_DIR}/winterberg/      ← Winterberg theory notes & analysis")
print(f"  {CORPUS_DIR}/lcf/             ← LCF experimental data & protocols")
print(f"  {CORPUS_DIR}/iccf/            ← ICCF paper annotations & critique")
print(f"  {CORPUS_DIR}/grid/            ← Grid application engineering analysis")
print(f"  {CORPUS_DIR}/negative/        ← Examples of what NOT to fabricate")
print()
print("Format: one JSON per line: {\"instruction\": ..., \"input\": ..., \"output\": ...}")
print("Minimum for meaningful fine-tune: 500 examples")
print("Target for strong proprietary behavior: 2000+ examples")
