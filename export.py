
import numpy as np


def exportSolutionToGmsh(file, dofManager, mesh, solution, prescribedNodes, prescribedValues):
    # Header
    file.write('$MeshFormat\n2.2 0 8\n$EndMeshFormat\n')

    file.write('$NodeData\n')
    file.write('1\n')
    file.write('\"Temperature field\"\n')
    file.write('1\n0.0\n3\n0\n1\n')
    file.write(str(mesh.npts) + '\n')

    for inode in range(mesh.npts):

        currdof = dofManager[inode]

        # If currdof is free
        if currdof > -1:
            currval = solution[currdof]
        else:
            # Otherwise, retrieve its fixed value
            # Quick'n dirty...
            mask = prescribedNodes == inode
            currval = prescribedValues[mask][0]

        file.write(str(inode + 1) + ' ' + str(currval) + '\n')

    # Footer
    file.write('$EndNodeData\n')



# def exportSolutionFluxToGmsh(file, dofManager, mesh, solution, prescribedNodes, prescribedValues):
#     # Header
#     file.write('$MeshFormat\n2.2 0 8\n$EndMeshFormat\n')
#
#     file.write('$NodeData\n')
#     file.write('1\n')
#     file.write('\"Temperature field\"\n')
#     file.write('1\n0.0\n3\n0\n1\n')
#     file.write(str(mesh.npts) + '\n')
#
#     for inode in range(mesh.npts):
#
#         currdof = dofManager[inode]
#
#         # If currdof is free
#         if currdof > -1:
#             currval = solution[currdof]
#         else:
#             # Otherwise, retrieve its fixed value
#             # Quick'n dirty...
#             mask = prescribedNodes == inode
#             currval = prescribedValues[mask][0]
#
#         file.write(str(inode + 1) + ' ' + str(currval) + '\n')
#
#     # Footer
#     file.write('$EndNodeData\n')
