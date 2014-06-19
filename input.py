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
    multiplicity = 1,  
    reactive=True,
    structure=SMILES("CCC=CCC=CCC"),
)
species(
    label='OH',
    multiplicity = 2, 
    reactive=True,
    structure=SMILES("[OH]"),
)
species(
    label='O2',
    multiplicity = 3, 
    reactive=True,
    structure=SMILES("[O][O]"),
)

# Reaction systems
simpleReactor(
    temperature=(298,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "nonadiene": 0.978,
        "OH": 0.003,
        "O2": 0.019
    },
    terminationTime=(5,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=1E-9,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=100000
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
