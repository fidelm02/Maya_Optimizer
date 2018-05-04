"""
Shading.

Description
"""
import General
reload (General)
from General import GeneralControls

import maya.cmds as cmds


class ShadingControls(GeneralControls):
    """
    Title.

    Description
    """

    def __init__(self):
        """
        Title.

        Description
        """
        # super(ShadingControls, self).__init__()
        GeneralControls.__init__(self)

    def repeated_shaders(self, fix):
        """
        Title.

        Description.
        """

        allShaders = cmds.ls(mat=1)
        uniqs = []
        repeated = []

        for Sh in allShaders:
            valid = True
            for unique in uniqs:
                if Sh == unique:
                    valid = False
                    repeated.append(Sh)
            if valid:
                uniqs.append(Sh)

        if len(repeated) == 0:
            self.details.append("No repeated shaders")
            self.posible_fix.append("No repeated shaders")
        else:
            self.posible_fix.append("Repeated shaders ")
            self.details.append("\t Repeated shaders: ")

            for el in repeated:
                self.details.append("\t    " + str(el))

        """
        if fix:
            self.posible_fix.append("repeated shaders fix")
        else:
            self.posible_fix.append("repeated shaders check")
        """

    def external_shaders(self, fix):
        """
        Title.

        Description.
        """
        allShaders = cmds.ls(mat=1)
        referenced = []

        for Sh in allShaders:
            if str(Sh).find(":") is not -1:
                referenced.append(Sh)

        if len(referenced) != 0:
            self.posible_fix.append("Referenced shader problems")
            self.details.append("\t Referenced shaders:")
            for refS in referenced:
                self.details.append("\t    " + str(refS))
        else:
            self.details.append("\t No referenced shaders")
            self.posible_fix.append("No referenced shaders")
        """
        if fix:
            self.posible_fix.append("external shaders fix")
        else:
            self.posible_fix.append("external shaders check")
        """

    def local_textures(self, fix):
        """
        Title.

        Description.
        """

        details = "\t Local textures: "
        problems = False
        problemFiles = []

        allFileNodes = cmds.ls(type = "file")
        problematicNodes = []
        for fileN in allFileNodes:
            pathF = cmds.getAttr(str(fileN) + ".fileTextureName")
            if pathF.find("C:/") is not -1:
                problematicNodes.append([str(fileN),pathF])
            if pathF.find("D:/") is not -1:
                problematicNodes.append([str(fileN) ,pathF])

        if len(problematicNodes) == 0:
            details = details + "Clear"
            self.posible_fix.append("Local textures clear")
            self.details.append("Local textures clear")
        else:
            self.posible_fix.append("Local textures problems: " + str(len(problematicNodes)))
            self.details.append("\t Textures problems: ")
            for pNode in problematicNodes:
                lineTex = "\t    " + pNode[0] + ": " + pNode[1]
                self.details.append(lineTex)
            """
            if fix:
                self.posible_fix.append("local textures fix")
            else:
                self.posible_fix.append("local check")
            """
