# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   Contact : Gregory LEGRAIN - gregory.legrain@ec-nantes.fr
#


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
