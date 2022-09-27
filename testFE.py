

from solveFE import solveFE

meshName = 'square10x10.msh'

# Setup the problem we want to solve
# Neumann boundary conditions : as a dictionary (~ stl map) (physicalId: qN value)
BCNs = {103:1}


# Dirichlet boundary conditions for lines : as a dictionary (~ stl map) (physicalId: uD value)
BCD_lns = {101:0}

# Dirichlet boundary conditions for nodes : as a dictionary (~ stl map) (physicalId: uD value)
BCD_nds = {}

# Conductivity (isotropic for example) : as a dictionary (~ stl map) (physicalId: Kfourier)
conductivities = {1000:202}

# Source term (constant for example) : as a lambda function, depending on
# the phydical coordinates.
# xyz is assumed to be a numpy array
sourceTerm = lambda x,y: 0

exportName = 'temperature.pos'

solveFE(meshName, conductivities, BCNs, BCD_lns, BCD_nds, sourceTerm, exportName)


