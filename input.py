# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'], #  'all', 'default'==['training'], [], 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    maximumRadicalElectrons = 2,
)

# List of species
species(
    label='nonadiene', 
    reactive=True,
    structure=SMILES("CCC=CCC=CCC"),
)
species(
    label='OH',
    reactive=True,
    structure=SMILES("[OH]"),
)
species(
    label='O2', 
    reactive=True,
    structure=SMILES("[O][O]"),
)

# Reaction systems
liquidReactor(
    temperature=(298,'K'),
    initialConcentrations={
        "nonadiene": (0.978e-3, 'mol/cm^3'),
        "OH": (0.003e-3, 'mol/cm^3'),
        "O2": (0.019e-3, 'mol/cm^3')
    },
    terminationTime=(5,'s'),
)

solvation(
    solvent = 'water'
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=1E-5,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=10000
)

# quantumMechanics(
#     software='mopac',
#     method='pm3',
#     # fileStore='QMfiles', # relative to where you run it from. Defaults to inside the output folder if not defined.
#     scratchDirectory = None, # not currently used
#     onlyCyclics = True,
#     maxRadicalNumber = 0,
#     )

options(
    units='si',
    saveRestartPeriod=(1,'hour'),
    drawMolecules=False,
    generatePlots=False,
)
