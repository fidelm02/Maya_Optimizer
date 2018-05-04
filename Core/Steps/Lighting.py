"""
Lighting.

Description
"""

import maya.cmds as cmds
import General
reload (General)
from General import GeneralControls

class LightingControls(GeneralControls):

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

    def external_lights(self, fix):
        """
        Title.

        Description.
        """

        lights = cmds.ls(lt = 1)
        ref_lights = []
        for lt in lights:
            if str(lt).find(":") is not -1:
                ref_lights.append(lt)
        if len(ref_lights) == 0:
            self.posible_fix.append("No external lights")
        else:
            self.posible_fix.append("External lights problem")
            self.details.append("\t External lights:")
            for lt2 in lights:
                self.details.append("\t    " + str(lt2))

        """
        if fix:
            self.posible_fix.append("external_lights fix")
        else:
            self.posible_fix.append("external_lights check")
        """

