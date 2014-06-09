# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'], #  'all', 'default'==['training'], [], 
    kineticsFamilies = ['!Intra_Disproportionation','!Substitution_O'],
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    maximumRadicalElectrons = 2,
)

# List of species
species(
    label='lin_acid',
    multiplicity = 1,  
    reactive=True,
    structure=SMILES("CCCCCC=CCC=CCCCCCCCC(=O)O"),
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
        "lin_acid": 0.98,
        "OH": 0.001,
        "O2": 0.019
    },
    terminationTime=(5,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.5,
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
