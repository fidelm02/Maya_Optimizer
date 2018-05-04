"""
Animation.

Description
"""

import General
reload (General)
from General import GeneralControls

import maya.cmds as cmds


class AnimationControls(GeneralControls):

    """
    Title.

    Description
    """

    def __init__(self):
        """
        Title.

        Description.
        """
        GeneralControls.__init__(self)

    def atom_nodes(self, fix):
        """
        Delete atom nodes.

        From the references, this method will delete all atom nodes
        """
        atom_list = cmds.ls(type='reference')

        atom_cantity = 0

        for current in atom_list:
            if str(current).count("tmpOfflineForAtomRN") > 0:
                atom_cantity = atom_cantity + 1
                if fix:
                    cmds.lockNode(current, l=0)
                    cmds.delete(current)

            if atom_cantity > 0:
                if fix:
                    self.posible_fix.append(
                        "\t" + str(atom_cantity) + "Atom nodes deleted.")
                else:
                    self.posible_fix.append(
                        "\t" + str(atom_cantity) + "Atom nodes in the scene.")
